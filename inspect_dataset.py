import pandas as pd

df = pd.read_csv("travel_data.csv")

print(df.head())
print("\nColumns:\n", df.columns)
print("\nTotal rows:", len(df))
