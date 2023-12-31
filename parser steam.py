from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import csv
import os

if os.path.isfile('names.csv'):
    os.remove('names.csv')
dict = {}
all_price = []
new_all_price = []
all_name = []

for i in range(1, 10):
    # Передал ссылку на сайт в переменную и получил html код
    url = f"https://steamcommunity.com/market/search?appid=730#&count=50&&q=p{i}_popular_desc"
    headers = {
        "Accept-Language": "en;q=0.9",
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.5.708 Yowser/2.5 Safari/537.36"
    }
    html = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(html.text, "lxml")
    # Получение кусков кода html
    name = soup.find_all("span", class_="market_listing_item_name")
    print(name)
    for k in name:
        all_name.append(k.text)

print(all_name)

df = pd.DataFrame(all_name)


df = pd.DataFrame(df)


gfg_csv_data = df.to_csv('names.csv', index = False)

print(df)

