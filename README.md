# SOD1 structure + confidence viewer

A small FastAPI app serving the computational SOD1 structure/confidence result from disk. The page uses Tailwind CSS and 3Dmol.js from CDNs.

## Run

From this folder:

```bash
uv run uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000/ in a browser.

The app reads `results/results.json` and serves the selected PDB/CIF from `results/` or `data/`. No database is used. The displayed dimer is a computational hypothesis and the confidence values do not establish mutation safety.
