import remoclient
from os.path import join, dirname
from dotenv import load_dotenv
import json
import pandas as pd

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

te_path = join(dirname(__file__), "./data/te.json")

df = pd.read_json(te_path)
df["created_at"] = pd.to_datetime(df["created_at"], utc=True)
# df.index = pd.DatetimeIndex(df["created_at"], name="valid_time")

# 最新データ取得
client = remoclient.NatureRemoClient()
events = client.get_newest_events().get("te")

# 取得データを追加
add_df = pd.DataFrame([events])
add_df["created_at"] = pd.to_datetime(add_df["created_at"], utc=True)

# 取得データをマージ
df = df.append(add_df)
df = df[~df.duplicated()]

# JSONに保存
df["created_at"] = df["created_at"].astype(str)
with open(te_path, "w") as f:
    json.dump(df.to_dict(orient="records"), f, indent=4)
