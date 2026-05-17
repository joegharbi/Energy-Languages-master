from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "results" / "analysis" / "data.csv"
OUTPUT_PATH = BASE_DIR / "results" / "analysis" / "ration1.csv"

df = pd.read_csv(DATA_PATH, sep=";", header=None)
df[2] = df[2] / 1e6
df[3] = df[3] * 1000
df["new_column"] = df[2] / df[3]
df[2] = df[2].round(3)
df[3] = df[3].round(3)
df["new_column"] = df["new_column"].round(3)
df.to_csv(OUTPUT_PATH, sep=";", header=False, index=False)
