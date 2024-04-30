import json
import pandas as pd

if __name__ == "__main__":
  with open('data/mvrv.json', 'r') as file:
    json = json.load(file)
    df = pd.DataFrame(json["mvrv"])
    df.columns = ["date", "mvrv"]
    df.to_csv('data/dataset.csv', index=False)
