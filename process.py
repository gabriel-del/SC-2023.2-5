import json
import pandas as pd

def f(name, index=None):
  if index is None: index = name
  with open(f'data/{name}.json', 'r') as file:
    json_file = json.load(file)
    df_1 = pd.DataFrame(json_file["market-price"])
    df_2 = pd.DataFrame(json_file[index])
    df_1.columns = ["date", "market-price"]
    df_2.columns = ["date", name]
    return pd.merge( df_1,df_2, on="date", how="outer")


df = pd.merge(
  f('mvrv'),
  f('200w', '200w-moving-avg-heatmap'),
  how="outer")
df = df.sort_values(by="date")
df["date"] = pd.to_datetime(df["date"], unit='ms').dt.strftime('%Y%m%d%H%M%S')
print(df)
df.to_csv('data/dataset.csv', index=False)
