from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any

# This app does not use the course API; prevent unrelated .env settings from
# being interpreted by Scanpy/anndata's settings configuration.
import os
os.environ.pop("DDLS_API_KEY", None)

import numpy as np
import pandas as pd
import scanpy as sc
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse

DATA_PATH = Path(__file__).parent / "data" / "pbmc3k.h5ad"


@asynccontextmanager
async def lifespan(app: FastAPI):
    if not DATA_PATH.exists():
        raise RuntimeError(f"Dataset not found: {DATA_PATH}")
    adata = sc.read_h5ad(DATA_PATH)
    adata.var_names_make_unique()
    app.state.adata = adata
    yield
    del app.state.adata


app = FastAPI(title="PBMC Explorer", lifespan=lifespan)

DEATH_RELATED_GENES = ["BAX", "BBC3", "PMAIP1", "DDIT3", "FOS", "JUN", "HSPA1A", "HSPA1B"]


def json_value(value: Any) -> Any:
    if isinstance(value, (np.integer, np.floating)):
        return value.item()
    return value


def dense_column(matrix: Any, index: int) -> np.ndarray:
    values = matrix[:, index]
    return values.toarray().ravel() if hasattr(values, "toarray") else np.asarray(values).ravel()


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    return HTML


@app.get("/api/umap")
def umap(cluster: str | None = None):
    adata = app.state.adata
    if "X_umap" not in adata.obsm:
        raise HTTPException(500, "Dataset has no UMAP coordinates")
    coords = np.asarray(adata.obsm["X_umap"])
    clusters = adata.obs["leiden"].astype(str) if "leiden" in adata.obs else pd.Series(["All"] * adata.n_obs)
    mask = np.ones(adata.n_obs, dtype=bool) if cluster in (None, "all") else (clusters == cluster).to_numpy()
    return {"points": [{"id": str(adata.obs_names[i]), "x": float(coords[i, 0]), "y": float(coords[i, 1]), "cluster": str(clusters.iloc[i])} for i in np.flatnonzero(mask)]}


@app.get("/api/genes")
def genes(q: str = Query("", max_length=100), limit: int = Query(50, ge=1, le=200)):
    names = [str(x) for x in app.state.adata.var_names if q.lower() in str(x).lower()]
    return {"genes": names[:limit]}


@app.get("/api/expression/{gene}")
def expression(gene: str):
    adata = app.state.adata
    matches = [i for i, name in enumerate(adata.var_names) if str(name).upper() == gene.upper()]
    if not matches:
        raise HTTPException(404, f"Unknown gene: {gene}")
    values = dense_column(adata.X, matches[0])
    return {"gene": str(adata.var_names[matches[0]]), "values": [float(x) for x in values]}


@app.get("/api/clusters")
def clusters():
    adata = app.state.adata
    if "leiden" not in adata.obs:
        raise HTTPException(500, "Dataset has no leiden clusters")
    result = []
    for cluster in sorted(adata.obs["leiden"].astype(str).unique(), key=lambda x: (int(x) if x.isdigit() else x)):
        mask = adata.obs["leiden"].astype(str).to_numpy() == cluster
        result.append({"cluster": cluster, "cells": int(mask.sum()), "quality": quality(adata, mask), "markers": markers(adata, mask)})
    return {"clusters": result}


def quality(adata, mask):
    fields = ["n_genes", "total_counts", "pct_mito"]
    return {field: {"mean": float(pd.to_numeric(adata.obs.loc[mask, field]).mean()), "median": float(pd.to_numeric(adata.obs.loc[mask, field]).median())} for field in fields if field in adata.obs}


def markers(adata, mask, n=10):
    values = adata.X[mask]
    means = values.mean(axis=0)
    means = np.asarray(means).ravel() if not hasattr(means, "toarray") else means.toarray().ravel()
    return [{"gene": str(adata.var_names[i]), "mean_expression": float(means[i])} for i in np.argsort(means)[::-1][:n]]


HTML = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>PBMC Explorer</title>
<script src="https://cdn.tailwindcss.com"></script><script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script></head>
<body class="bg-slate-100 text-slate-900"><main class="mx-auto max-w-7xl p-4 sm:p-6"><h1 class="mb-1 text-2xl font-bold">PBMC Explorer</h1><p class="mb-4 text-sm text-slate-600">Explore UMAP clusters, gene expression, markers, and quality.</p>
<section class="grid gap-4 lg:grid-cols-[19rem_1fr_20rem]"><aside class="space-y-4 rounded-xl bg-white p-4 shadow"><label class="block text-sm font-medium">Cluster<select id="cluster" class="mt-1 w-full rounded border p-2"><option value="all">All clusters</option></select></label><fieldset class="rounded border p-3"><legend class="px-1 text-sm font-medium">Genes indicating cell death</legend><div id="death-genes" class="mt-1 space-y-2"></div><div class="mt-3 border-t pt-3 text-xs text-slate-600"><p class="mb-1 font-semibold text-slate-700">Single best identifying gene</p><ul class="space-y-1"><li>Cluster 0: <strong>CD3D</strong></li><li>Cluster 1: <strong>S100A8</strong></li><li>Cluster 2: <strong>NKG7</strong></li><li>Cluster 3: <strong>MS4A1</strong></li><li>Cluster 4: <strong>FCGR3A</strong></li><li>Cluster 5: <strong>FCER1A</strong></li><li>Cluster 6: <strong>PPBP</strong></li><li>Cluster 7: <strong>STMN1</strong></li></ul></div></fieldset><label class="block text-sm font-medium">Gene expression<input id="gene" list="gene-list" placeholder="e.g. CD3D" class="mt-1 w-full rounded border p-2"><datalist id="gene-list"></datalist></label><button id="reset" class="w-full rounded bg-indigo-600 px-3 py-2 text-white hover:bg-indigo-700">Reset</button><div id="details" class="text-sm"></div></aside><section class="min-w-0 self-start rounded-xl bg-white p-2 shadow"><div id="plot" class="h-[55vh] min-h-[20rem]"></div></section><aside class="self-start space-y-4 rounded-xl bg-white p-4 shadow"><h2 class="text-lg font-semibold">Research questions</h2><article class="border-b pb-4"><h3 class="font-semibold">1. Can cluster 6 be removed?</h3><p class="mt-2 text-sm text-slate-700"><strong>No.</strong> Cluster 6 should not be removed as dead cells based on the available evidence. Its quality controls should be compared with the other clusters, and its expression of the cell-death indicator genes should be checked. The evidence does not support the conclusion that cluster 6 consists only of dead cells.</p><p class="mt-2 text-xs text-slate-500">The interview records that the original suspicion was based mainly on the small cluster size and low gene count, not on a direct viability measurement.</p></article><article><h3 class="font-semibold">2. Can clusters 1 and 2 be paired?</h3><p class="mt-2 text-sm text-slate-700"><strong>No.</strong> They should remain separate. They occupy distinct regions of the UMAP and show different expression profiles. For example, cluster 1 is characterized by genes such as <strong>LYZ</strong>, <strong>S100A8</strong>, and <strong>FTL</strong>, whereas cluster 2 is characterized by genes such as <strong>NKG7</strong>, <strong>GZMA</strong>, and <strong>CCL5</strong>.</p><p class="mt-2 text-xs text-slate-500">The UMAP separation supports keeping them distinct, while marker expression provides biological evidence for the difference.</p></article></aside></section></main>
<script>
const $=id=>document.getElementById(id); let points=[];
const deathGenes=['BAX','BBC3','PMAIP1','DDIT3','FOS','JUN','HSPA1A','HSPA1B'];
async function load(){const [u,c]=await Promise.all([fetch('/api/umap').then(r=>r.json()),fetch('/api/clusters').then(r=>r.json())]);points=u.points; c.clusters.forEach(x=>{cluster.append(new Option(`Cluster ${x.cluster} (${x.cells})`,x.cluster));});$('death-genes').innerHTML=deathGenes.map(g=>`<label class="flex items-center gap-2"><input type="checkbox" value="${g}" class="death-gene rounded" onchange="draw()"><span>${g}</span></label>`).join(''); details.innerHTML=c.clusters.map(x=>`<details class="border-b py-2"><summary class="cursor-pointer font-semibold">Cluster ${x.cluster}</summary><p>${Object.entries(x.quality).map(([k,v])=>`${k}: ${v.mean.toFixed(1)}`).join('<br>')}</p><p class="mt-1 text-xs">Markers: ${x.markers.map(m=>m.gene).join(', ')}</p></details>`).join(''); draw();}
async function draw(){let data=points;const cl=cluster.value;if(cl!=='all')data=data.filter(p=>p.cluster===cl);const typedGene=geneInput();const selectedGene=[...document.querySelectorAll('.death-gene:checked')].map(x=>x.value)[0];const activeGene=selectedGene||typedGene;const explicitlySelected=Boolean(selectedGene||typedGene&&document.getElementById('gene').dataset.selected==='true');if(activeGene&&explicitlySelected){const e=await fetch('/api/expression/'+encodeURIComponent(activeGene));if(e.ok){const j=await e.json();data=data.map(p=>({...p,value:j.values[points.findIndex(q=>q.id===p.id)]}));}}const expressionMode=Boolean(activeGene&&explicitlySelected);Plotly.react('plot',[{x:data.map(p=>p.x),y:data.map(p=>p.y),mode:'markers',type:'scattergl',text:data.map(p=>`${p.id}<br>Cluster ${p.cluster}`),customdata:expressionMode?data.map(p=>p.value):undefined,marker:{size:6,color:expressionMode?data.map(p=>p.value):data.map(p=>p.cluster),colorscale:'Viridis',showscale:expressionMode,colorbar:{title:expressionMode?activeGene:''}}}],{margin:{t:20,r:10,b:45,l:45},xaxis:{title:'UMAP 1'},yaxis:{title:'UMAP 2'},hovermode:'closest'});}
function geneInput(){return $('gene').value.trim();} $('cluster').onchange=draw;$('gene').onchange=()=>{$('gene').dataset.selected='true';draw();};$('gene').oninput=async()=>{if(!$('gene').value.trim()){$('gene').dataset.selected='false';draw();}let q=$('gene').value;let r=await fetch('/api/genes?q='+encodeURIComponent(q));$('gene-list').innerHTML=(await r.json()).genes.map(x=>`<option value="${x}">`).join('');};document.addEventListener('change',event=>{if(event.target.classList.contains('death-gene')&&event.target.checked){document.querySelectorAll('.death-gene').forEach(box=>{if(box!==event.target)box.checked=false;});$('gene').value='';$('gene').dataset.selected='false';draw();}});$('reset').onclick=()=>{$('cluster').value='all';$('gene').value='';$('gene').dataset.selected='false';document.querySelectorAll('.death-gene').forEach(box=>box.checked=false);draw()};load();
</script></body></html>'''
