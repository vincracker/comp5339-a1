# NSW EV charging data pipeline

Four notebooks acquire NSW charger locations and ABS SA4 boundaries, clean the
records, enrich DC chargers with Open Charge Map/OpenStreetMap data, and build a
DuckDB database.

## Setup

Python 3.13 is recommended (minimum: 3.12). Run these commands from the
repository root (`comp5339-a1`).
Dependencies are declared in `pyproject.toml` and mirrored in `requirements.txt`
for pip. Keep `pyproject.toml` in the root; the notebooks use it to locate data.

**Windows (PowerShell):**

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m jupyterlab
```

**macOS/Linux:**

```bash
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m jupyterlab
```

## Run the notebooks

In JupyterLab, open each notebook below, select the Python kernel from `.venv`,
and use **Kernel → Restart Kernel and Run All Cells**. Wait for each notebook to
finish successfully before starting the next.

| Order | Notebook | Main outputs |
| --- | --- | --- |
| 1 | [data_acquisition.ipynb](notebooks/data_acquisition.ipynb) | Charger CSV, SA4 shapefile, and provenance manifest in `data/raw/`. |
| 2 | [integration_quality_B.ipynb](notebooks/integration_quality_B.ipynb) | Cleaned records, power components, and quality summary in `data/interim/`. |
| 3 | [data_augmentation.ipynb](notebooks/data_augmentation.ipynb) | DC subset, augmented DC records, and augmentation summary in `data/interim/`. |
| 4 | [data_transformation_and_storage.ipynb](notebooks/data_transformation_and_storage.ipynb) | `data/processed/ev_chargers.duckdb`, containing augmented DC and retained non-DC records. |

Internet access is required for acquisition and the first DuckDB `spatial`
extension installation. No separate database server or GIS software is needed.

Augmentation reuses the two committed CSV caches in `data/external/` by default;
no API key is needed when both are present. If the Open Charge Map cache is
missing or you want to refresh it, copy `.env.example` to `.env`, set
`OPENCHARGEMAP_API_KEY`, and restart the augmentation notebook. To refresh existing
caches, also set `FORCE_REFETCH = True` in that notebook. Overpass needs no key.
Keep `.env` private.

Leave `FORCE_DOWNLOAD` and `FORCE_REFETCH` set to `False` to reuse cached data.
Cleaning expects the December 2025 charger snapshot with 1,958 rows; a changed
source release may fail its validation checks. Close connections to the output
database before rerunning the storage notebook, which rebuilds it. Generated
raw, interim, and processed files are Git-ignored; include the final `.duckdb`
file separately when submitting the project.
