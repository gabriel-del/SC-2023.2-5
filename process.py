import json
import pandas as pd

def a():
  with open('data/mvrv.json', 'r') as file:
    json_file = json.load(file)
    df_mvrv = pd.DataFrame(json_file["mvrv"])
    df_market_price = pd.DataFrame(json_file["market-price"])
    df_mvrv.columns = ["date", "mvrv"]
    df_market_price.columns = ["date", "market-price"]
    return pd.merge( df_market_price,df_mvrv, on="date", how="outer")

def b():
  with open('data/200w.json', 'r') as file:
    json_file = json.load(file)
    df_2 = pd.DataFrame(json_file["200w-moving-avg-heatmap"])
    df_1 = pd.DataFrame(json_file["market-price"])
    df_2.columns = ["date", "200w"]
    df_1.columns = ["date", "market-price"]
    return pd.merge( df_1,df_2, on="date", how="outer")


df = pd.merge( a(),b(), how="outer")
df = df.sort_values(by="date")
df["date"] = pd.to_datetime(df["date"], unit='ms').dt.strftime('%Y%m%d%H%M%S')
print(df)
df.to_csv('data/dataset.csv', index=False)
