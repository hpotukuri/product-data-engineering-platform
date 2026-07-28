import pandas as pd
from src.common.logger import logger

def read_csv(path: str):
    logger.info(f"Reading {path}")

    return pd.read_csv(path)