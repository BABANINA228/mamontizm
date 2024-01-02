from bs4 import BeautifulSoup
import requests
import time
import csv
import json
import os

all_name = []
start = 0
count = 50
for i in range(9):
    url = f"https://steamcommunity.com/market/search/render/?query=&start={start}&count={count}&search_descriptions=0&sort_column=popular&sort_dir=desc&appid=730"
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.5.708 Yowser/2.5 Safari/537.36"}
    html = requests.get(url = url, headers = headers)

    # with open('html.html', 'w') as file:
    #     file.write(html.text)

    soup = BeautifulSoup(html.json().get("results_html"), "lxml")
    # print(soup)
    name = soup.find_all("span", class_ = "market_listing_item_name")
    # Получение цены и имени
    for k in name:
        all_name.append(k.text)
    start += 50
    count += 50
with open('test.txt', 'w') as file:
    for i in all_name:
        file.write(f'{i}\n')
# csv.register_dialect('my_di', lineterminator="\r", delimiter=0, quotechar=' ')
# with open("information.csv", "a", encoding = "utf-8") as file:
#     writer = csv.writer(file, 'my_di')
#     writer.writerow(all_name[1])