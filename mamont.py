import pandas as pd
import csv
import requests
from urllib.parse import quote
import time

url = 'https://steamcommunity.com/market/priceoverview/?appid=730&currency=5&market_hash_name='

with open('names.csv', newline='') as f:
    reader = csv.reader(f)
    names = list(reader)
names.pop(0)
print(names)

for i in names:
    time.sleep(1)
    url = 'https://steamcommunity.com/market/priceoverview/?appid=730&currency=5&market_hash_name='
    hash_name = quote(str(i[0]))
    url = url + hash_name
    print(url)
    html = requests.get(url)
    print(html.json())