from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "results" / "analysis" / "data.csv"
OUTPUT_PATH = BASE_DIR / "results" / "analysis" / "norm_by_function_and_c.csv"

column_names = ["Language", "Function", "Energy consumption in microjoules", "Runtime in seconds"]
df = pd.read_csv(DATA_PATH, names=column_names, sep=";")
mean_df = df.groupby(["Language", "Function"]).mean()
c_values = mean_df.loc["c"]
normalized_df = mean_df / c_values
normalized_df.reset_index(inplace=True)
normalized_df.to_csv(OUTPUT_PATH, index=False)
