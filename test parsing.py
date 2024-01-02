from bs4 import BeautifulSoup
import pandas as pd
import requests
import os

all_name = []

url = "https://steamcommunity.com/market/search/render/?query=&start=0&count=500&search_descriptions=0&sort_column=popular&sort_dir=desc&appid=730"
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.5.708 Yowser/2.5 Safari/537.36"}
html = requests.get(url = url, headers = headers)

# with open('html.html', 'w') as file:
#     file.write(html.json().get('results_html'))

soup = BeautifulSoup(html.json().get('results_html'), "lxml")
    # Получение кусков кода html
name = soup.find_all("span", class_ = "market_listing_item_name")
   # Получение цены и имени
for k in name:
    all_name.append(k.text)
# print(all_name)
print(all_name)

df = pd.DataFrame(all_name)
gfg_csv_data = df.to_csv('names.csv', index = False)