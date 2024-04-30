import json
import pandas as pd

def json_to_csv(json, csv):
  df = pd.DataFrame(json["mvrv"])
  df.columns = ["date", "mvrv"]
  df.to_csv(csv, index=False)

if __name__ == "__main__":
  with open('data/mvrv.json', 'r') as file:
    json = json.load(file)
    json_to_csv(json, 'data/dataset.csv')
