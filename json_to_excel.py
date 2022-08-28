#%%
import pandas as pd
import json
import numpy as np

from datetime import datetime

#%%
file_path = "data/eur-rub.json"
column_name = "Цена EURO, руб"

#%%
with open(file_path, "r") as f:
    file = json.load(f)

#%%
for instance in file:
    date = datetime.fromtimestamp(instance["date"])
    month = str(date.month)
    date_s = f"{date.year}-{month if len(month) == 2 else f'0{month}'}-01"
    instance["date"] = date_s

#%%
df = pd.read_excel("data/Train-m.xlsx", header=0)

#%%
df_new = pd.DataFrame(file, index=range(len(file))).drop(["price_open", "price_high", "price_low", "price_close"], axis=1)
df_new = df_new[df_new["date"].isin(df["date"].values)]
df_new.columns = ["date", column_name]
print(df_new.head(3))

#%%
pd.merge(df, df_new, on="date").to_excel("data/Train-m.xlsx", index=False)
