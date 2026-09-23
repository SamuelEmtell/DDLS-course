# DDLS Course

This repository contains work from the DDLS course, organized by week:

- **[Week4](Week4/)** – Week 4 course work on protein structure prediction and analysis.
- **[Week5](Week5/)** – Week 5 single-cell RNA-seq exploration and cell-cluster quality analysis.

## Week 5

The Week 5 app is a Streamlit application for exploring the PBMC 3k single-cell RNA-seq dataset. It supports interactive inspection of the data, dimensionality-reduction visualizations, clustering, and cluster-quality analysis.

### Run the app locally

From the repository root:

```bash
cd Week5
python -m venv .venv
source .venv/bin/activate       # macOS/Linux
# .venv\\Scripts\\activate    # Windows
pip install -r requirements.txt
streamlit run app.py
```

The terminal will provide a local URL, usually `http://localhost:8501`.

The dataset is stored in `Week5/data/pbmc3k.h5ad`. Submission materials, including the app archive and analysis transcripts, are in `Week5/submissions/`.

## Repository structure

```text
Week4/       Week 4 files, data, scripts, and results
Week5/       Week 5 app, data, documentation, and submissions
```

Local environments, caches, secrets, and other machine-specific files should not be committed.
