from src.common.constants import RAW_FOLDER
from src.common.file_reader import read_csv

customers = read_csv(RAW_FOLDER / "customers.csv")

print(customers)