from functools import wraps
import requests 
import json
import pandas as pd 


URL = "https://sanctions.nazk.gov.ua/en/api/v4/person/"
def fetch_data(URL:str) -> pd.DataFrame:
    response = requests.get(URL, headers={'User-Agent': 'Your-User-Agent', 'Accept':'application/json'}, stream=True)
    data = json.loads(response.text)
    df = pd.json_normalize(data["data"], max_level=1)
    return df

df = fetch_data(URL)
print(df)
