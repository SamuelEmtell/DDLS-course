"""Print per-cluster quality summaries for the PBMC h5ad dataset."""
from pathlib import Path

import pandas as pd
import scanpy as sc

DATA_PATH = Path(__file__).parent / "data" / "pbmc3k.h5ad"
QUALITY_COLUMNS = ["n_genes", "total_counts", "pct_mito"]


def main() -> None:
    adata = sc.read_h5ad(DATA_PATH)

    if "leiden" not in adata.obs:
        raise SystemExit("The dataset does not contain an obs['leiden'] column.")

    missing = [column for column in QUALITY_COLUMNS if column not in adata.obs]
    if missing:
        raise SystemExit(f"Missing quality columns: {', '.join(missing)}")

    # Convert values to numeric in case they were stored as strings/categories.
    quality = adata.obs[QUALITY_COLUMNS].apply(pd.to_numeric, errors="coerce")
    clusters = adata.obs["leiden"].astype(str)

    summary = quality.groupby(clusters).agg(["count", "mean", "median", "min", "max"])
    summary.insert(0, "cells", clusters.value_counts().reindex(summary.index).astype(int))

    # Print one readable table per metric.
    print(f"Dataset: {DATA_PATH}")
    print(f"Total cells: {adata.n_obs}")
    print("\nPer-cluster quality summary:\n")
    print(summary.round(2).to_string())

    print("\nCluster means only:\n")
    means = quality.groupby(clusters).mean().round(2)
    means.insert(0, "cells", clusters.value_counts().reindex(means.index).astype(int))
    print(means.to_string())


if __name__ == "__main__":
    main()
