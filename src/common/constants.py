from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATASETS_FOLDER = PROJECT_ROOT / "datasets"

RAW_FOLDER = DATASETS_FOLDER / "raw"

BRONZE_FOLDER = DATASETS_FOLDER / "bronze"

SILVER_FOLDER = DATASETS_FOLDER / "silver"

GOLD_FOLDER = DATASETS_FOLDER / "gold"