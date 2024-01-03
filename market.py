from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
from urllib.parse import quote
import time
import os


names = pd.read_csv("names.csv")
names = names.values.tolist()

# for i in range(1):
#     url = 'https://market.csgo.com/api/v2/search-item-by-hash-name?key=42N05ro4gln24tP198b6A5F2Uu5h3ha&hash_name='
#     hash_name = quote(names[i][0])
#     url = url + hash_name
#     html = requests.get(url)
    # print(url)


from csgo_market_api import CSGOMarket

market = CSGOMarket(api_key='42N05ro4gln24tP198b6A5F2Uu5h3ha')
list_hash_name = [names[2][0]]
item_info = market.get_list_items_info(list_hash_name=list_hash_name)
print(item_info['data'][names[2][0]]['average'])


    # with open('html.html', 'w') as file:
    #     file.write(html.text)
    # soup = BeautifulSoup(html.text, "lxml")

    # price = soup.find("div", class_ = "mat-h2 title")
    # print(price)
# def get_info(name):
#     url = 'https://steamcommunity.com/market/priceoverview/?appid=730&currency=5&market_hash_name='
#     hash_name = quote(name)
#     url = url + hash_name
#     html = requests.get(url)
#     

# get_info(names[2][0])
        

# API ключ к маркету 42N05ro4gln24tP198b6A5F2Uu5h3ha