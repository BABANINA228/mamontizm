from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

all_name = []
start = 0
count = 50
for i in range(10):
    time.sleep(1)
    url = f"https://steamcommunity.com/market/search/render/?query=&start={start}&count={count}&search_descriptions=0&sort_column=popular&sort_dir=desc&appid=730"
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.5.708 Yowser/2.5 Safari/537.36"}
    html = requests.get(url = url, headers = headers)

    soup = BeautifulSoup(html.json().get("results_html"), "lxml")
    name = soup.find_all("span", class_ = "market_listing_item_name")
    # Получение цены и имени
    for k in name:
        all_name.append(k.text)
    start += 50
    count += 50

df = pd.DataFrame(all_name)
df.to_csv("names.csv")

