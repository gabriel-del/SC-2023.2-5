import json
import pandas as pd

with open('data/mvrv.json', 'r') as file:
  json = json.load(file)
  df_mvrv = pd.DataFrame(json["mvrv"])
  df_market_price = pd.DataFrame(json["market-price"])
  df_mvrv.columns = ["date", "mvrv"]
  df_market_price.columns = ["date", "market-price"]
  df = pd.merge( df_market_price,df_mvrv, on="date", how="outer")
  df = df.sort_values(by="date")
  df["date"] = pd.to_datetime(df["date"], unit='ms').dt.strftime('%Y%m%d%H%M%S')
  print(df)
  df.to_csv('data/dataset.csv', index=False)
