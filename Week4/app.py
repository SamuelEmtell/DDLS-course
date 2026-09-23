from pathlib import Path
import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, Response

ROOT = Path(__file__).parent
RESULTS = ROOT / "results"
DATA = ROOT / "data"
app = FastAPI(title="SOD1 Structure + Confidence Viewer")


def read_results():
    return json.loads((RESULTS / "results.json").read_text())


@app.get("/", response_class=HTMLResponse)
def index():
    return HTMLResponse(INDEX_HTML)


@app.get("/api/results")
def api_results():
    return JSONResponse(read_results())


@app.get("/structure/{name}")
def structure(name: str):
    if Path(name).name != name or Path(name).suffix.lower() not in {".pdb", ".cif"}:
        raise HTTPException(404, "Structure not found")
    path = RESULTS / name
    if not path.is_file():
        path = DATA / name
    if not path.is_file():
        raise HTTPException(404, "Structure not found")
    media = "chemical/x-pdb" if path.suffix.lower() == ".pdb" else "chemical/x-mmcif"
    return Response(path.read_bytes(), media_type=media)


INDEX_HTML = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SOD1 structure confidence viewer</title>
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://3Dmol.csb.pitt.edu/build/3Dmol-min.js"></script>
<style>body{background:#f8fafc}.viewer{height:620px;width:100%;position:relative;overflow:hidden}.viewer canvas{display:block!important;width:100%!important;height:100%!important}.chart{height:360px;width:100%}.chart canvas{display:block;width:100%;height:100%}.mono{font-variant-numeric:tabular-nums}</style></head>
<body class="text-slate-900"><main class="max-w-7xl mx-auto px-5 py-8">
<header class="mb-7"><p class="text-sm font-semibold tracking-wide text-indigo-600 uppercase">Structure + confidence viewer</p><h1 class="text-3xl font-bold mt-2">Human SOD1 mutagenesis screen</h1><p class="mt-2 text-slate-600">A readable view of the supplied model, local confidence, and predicted interface evidence.</p></header>
<section class="grid lg:grid-cols-[1.4fr_1fr] gap-5 mb-5"><article class="bg-white rounded-2xl shadow-sm ring-1 ring-slate-200 p-6"><div class="flex gap-3"><svg class="w-6 h-6 text-indigo-600 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3 4 7.5v9L12 21l8-4.5v-9L12 3Z"/><path d="m4 7.5 8 4.5 8-4.5M12 12v9"/></svg><div><h2 class="text-sm font-semibold text-slate-500 uppercase tracking-wide">Headline answer</h2><p id="headline" class="text-xl font-semibold mt-2"></p></div></div></article><article class="bg-white rounded-2xl shadow-sm ring-1 ring-slate-200 p-6"><h2 class="text-sm font-semibold text-slate-500 uppercase tracking-wide">Structure check</h2><p id="structure-check" class="mt-3 text-slate-700"></p></article></section>
<section class="grid xl:grid-cols-[1.05fr_1fr] gap-6 items-stretch"><article class="bg-white rounded-2xl shadow-sm ring-1 ring-slate-200 overflow-hidden flex flex-col"><div class="p-5 border-b border-slate-100 flex justify-between items-center"><div><h2 class="font-bold text-lg">3D predicted assembly</h2><p class="text-sm text-slate-500">Blue = chain A · orange = chain B · sticks = highlighted residues</p></div><span id="assembly" class="text-xs px-2 py-1 rounded-full bg-slate-100 text-slate-600"></span></div><div id="viewer" class="viewer bg-slate-950 flex-1"></div><div class="p-4 text-xs text-slate-500">Cartoon representation. This is a computational two-chain hypothesis, not an experimentally validated assembly.</div></article>
<article class="bg-white rounded-2xl shadow-sm ring-1 ring-slate-200 p-6 flex flex-col"><div class="flex items-start justify-between"><div><h2 class="font-bold text-xl">Confidence matched to the claim</h2><p class="text-sm text-slate-500 mt-1">Per-residue pLDDT for local fold confidence</p></div><div class="text-right mono text-base"><div><span class="text-slate-500">min</span> <b id="min" class="text-lg"></b></div><div><span class="text-slate-500">mean</span> <b id="mean" class="text-lg"></b></div></div></div><div class="chart mt-6 flex-1 min-h-[360px]"><canvas id="plddt" aria-label="Per-residue pLDDT chart; horizontal axis is residue number"></canvas></div><p class="text-sm font-medium text-slate-600 mt-2">Horizontal axis: residue number (1–154)</p><div class="mt-4 flex gap-4 text-xs text-slate-500"><span><i class="inline-block w-3 h-3 rounded-full bg-indigo-600 mr-1"></i>pLDDT</span><span><i class="inline-block w-3 h-3 rounded-full bg-rose-500 mr-1"></i>metal-binding residues</span></div><div class="mt-5 pt-4 border-t border-slate-100"><h3 class="font-semibold text-sm">Interface evidence</h3><div class="grid grid-cols-2 gap-3 mt-3 text-sm"><div class="bg-slate-50 rounded-lg p-3"><span class="text-slate-500">Interface PAE mean</span><b id="ipae" class="block text-lg"></b></div><div class="bg-slate-50 rounded-lg p-3"><span class="text-slate-500">Interface PAE min</span><b id="ipae-min" class="block text-lg"></b></div></div><p class="text-xs text-slate-500 mt-3">Lower PAE means the predicted relative placement is more confident. It does not prove biological binding.</p></div></article></section>
<section class="mt-5 bg-amber-50 border border-amber-200 rounded-2xl p-5"><div class="flex gap-3"><svg class="w-6 h-6 text-amber-700 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3 2.8 20h18.4L12 3Z"/><path d="M12 9v5m0 3h.01"/></svg><div><h2 class="font-bold text-amber-900">Important caveat</h2><p id="caveat" class="mt-1 text-amber-900"></p></div></div></section>
<section class="mt-5 bg-white rounded-2xl shadow-sm ring-1 ring-slate-200 p-5"><div class="flex items-center justify-between gap-4"><div><h2 id="candidate-title" class="font-bold text-xl">Provisional computational candidates <span id="candidate-count" class="text-indigo-600"></span></h2><p id="candidate-warning" class="text-sm text-amber-700 mt-1"></p></div><svg class="w-7 h-7 text-indigo-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 19V5m0 14h16M8 16v-4m4 4V7m4 9v-6"/></svg></div><p id="candidate-filter" class="text-sm text-slate-500 mt-3"></p><div class="overflow-x-auto mt-4"><table class="w-full text-sm"><thead class="text-left text-xs uppercase tracking-wide text-slate-500 border-b border-slate-200"><tr><th class="py-2 pr-4">Position</th><th class="py-2 pr-4">Residue</th><th class="py-2 pr-4">AF pLDDT</th><th class="py-2 pr-4">Dimer pLDDT</th><th class="py-2 pr-4">Monomer SASA</th><th class="py-2 pr-4">SASA loss</th><th class="py-2">Cross-chain PAE</th></tr></thead><tbody id="candidate-table"></tbody></table></div></section>
<section class="mt-5 bg-white rounded-2xl shadow-sm ring-1 ring-slate-200 p-5"><h2 class="font-bold">Metal-binding residues</h2><p id="claimed-label" class="text-sm text-slate-500 mt-1"></p><div id="residues" class="flex flex-wrap gap-2 mt-3"></div></section>
<section class="mt-5 bg-slate-900 text-slate-100 rounded-2xl p-6"><div class="flex gap-3"><svg class="w-6 h-6 text-indigo-300 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3v18M3 12h18"/><circle cx="12" cy="12" r="8"/></svg><div><h2 class="font-bold text-lg">Would do if we had more time</h2><p id="future-purpose" class="text-slate-300 text-sm mt-1"></p><ul id="future-list" class="list-disc ml-5 mt-3 space-y-1 text-sm text-slate-300"></ul><p id="future-limit" class="text-amber-300 text-sm mt-4"></p></div></div></section><footer class="mt-8 text-xs text-slate-500">Evidence source: <code>results/results.json</code>. This viewer presents computational evidence and limitations; it does not establish mutation safety.</footer></main>
<script>
const $=id=>document.getElementById(id);
function drawChart(values, claimed){const c=$("plddt"),d=devicePixelRatio||1,r=c.parentElement.getBoundingClientRect();c.width=r.width*d;c.height=r.height*d;const x=c.getContext("2d");x.scale(d,d);const w=r.width,h=r.height,p={l:48,r:18,t:18,b:38};const X=i=>p.l+i*(w-p.l-p.r)/(values.length-1),Y=v=>p.t+(100-v)*(h-p.t-p.b)/60;x.strokeStyle="#cbd5e1";x.fillStyle="#64748b";x.font="11px system-ui";[50,70,90,100].forEach(v=>{x.beginPath();x.moveTo(p.l,Y(v));x.lineTo(w-p.r,Y(v));x.stroke();x.fillText(v,4,Y(v)+4)});x.strokeStyle="#4f46e5";x.lineWidth=2;x.beginPath();values.forEach((v,i)=>i?x.lineTo(X(i),Y(v)):x.moveTo(X(i),Y(v)));x.stroke();claimed.forEach(n=>{const i=n-1;x.fillStyle="#f43f5e";x.beginPath();x.arc(X(i),Y(values[i]),4,0,Math.PI*2);x.fill()});x.fillStyle="#64748b";x.fillText("Residue number",w/2-42,h-8);x.textAlign="center";[1,25,50,75,100,125,154].forEach(n=>{const i=n-1;x.fillText(String(n),X(i),h-22)});x.textAlign="start"}
async function init(){const r=await (await fetch('/api/results')).json();$('headline').textContent=r.headline;$('structure-check').textContent=r.structure_check;$('caveat').textContent=r.caveat;$('assembly').textContent=r.chains.map(c=>c.id+': '+c.length).join(' · ');$('min').textContent=r.plddt_summary.min.toFixed(2);$('mean').textContent=r.plddt_summary.mean.toFixed(2);$('ipae').textContent=r.interface_pae_mean.toFixed(2)+' Å';$('ipae-min').textContent=r.interface_pae_min.toFixed(2)+' Å';$('claimed-label').textContent=r.claimed_residue_label;r.claimed_residues.forEach(n=>{const s=document.createElement('span');s.className='px-3 py-1 rounded-full bg-rose-100 text-rose-700 text-sm font-semibold';s.textContent='H'+n;$('residues').append(s)});drawChart(r.plddt,r.claimed_residues);if(r.future_work){$('future-purpose').textContent=r.future_work.purpose;$('future-limit').textContent=r.future_work.limitation;r.future_work.steps.forEach(step=>{const li=document.createElement('li');li.textContent=step;$('future-list').append(li)})}if(r.candidate_section){$('candidate-title').firstChild.textContent=r.candidate_section.title+' ';$('candidate-count').textContent='('+r.candidate_section.candidates.length+' / '+(r.candidate_section.total_viable ?? r.candidate_section.candidates.length)+')';$('candidate-warning').textContent=r.candidate_section.warning;$('candidate-filter').textContent='Filter: '+r.candidate_section.filter;const tbody=$('candidate-table');r.candidate_section.candidates.forEach(c=>{const tr=document.createElement('tr');tr.className='border-b border-slate-100';tr.innerHTML=`<td class="py-2 pr-4 font-semibold">${c.position}</td><td class="py-2 pr-4 font-mono">${c.aa}</td><td class="py-2 pr-4">${c.af_plddt.toFixed(2)}</td><td class="py-2 pr-4">${c.dimer_plddt.toFixed(2)}</td><td class="py-2 pr-4">${c.monomer_sasa.toFixed(1)} Å²</td><td class="py-2 pr-4">${c.sasa_loss.toFixed(1)} Å²</td><td class="py-2">${c.cross_pae_mean.toFixed(2)} Å</td>`;tbody.append(tr)})}const v=$3Dmol.createViewer('viewer',{backgroundColor:'#020617',resize:true});const model=v.addModel(await (await fetch('/structure/'+r.structure_file)).text(),'pdb');v.setStyle({},{cartoon:{colorscheme:{prop:'b',gradient:'roygb',min:50,max:100}}});r.claimed_residues.forEach(n=>{v.setStyle({resi:n},{stick:{radius:.22,color:'#fb7185'},sphere:{radius:.45,color:'#fb7185'}});v.setStyle({chain:'B',resi:n},{stick:{radius:.22,color:'#fb7185'},sphere:{radius:.45,color:'#fb7185'}})});v.zoomTo();v.zoom(1.25);v.resize();v.render();window.addEventListener('resize',()=>{drawChart(r.plddt,r.claimed_residues);v.resize();v.zoomTo();v.zoom(1.25);v.render()})}init();
</script></body></html>'''
