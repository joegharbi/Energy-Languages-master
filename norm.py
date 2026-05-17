from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "results" / "analysis" / "data.csv"
OUTPUT_PATH = BASE_DIR / "results" / "analysis" / "nrom_by_c.csv"

column_names = ["Language", "Function", "Energy consumption in microjoules", "Runtime in seconds"]
df = pd.read_csv(DATA_PATH, names=column_names, sep=";")
numeric_columns = ["Energy consumption in microjoules", "Runtime in seconds"]
mean_df = df.groupby("Language")[numeric_columns].mean()
c_values = mean_df.loc["c"]
normalized_df = mean_df / c_values
normalized_df.to_csv(OUTPUT_PATH)
