import pandas as pd
import time
from csgo_market_api import CSGOMarket

# Больше 5 запросов в секунду не отправлять! Иначе ключ удалится

names = pd.read_csv("names.csv")
names = names.values.tolist()

market = CSGOMarket(api_key='42N05ro4gln24tP198b6A5F2Uu5h3ha')

for i in range(10):
    list_hash_name = [names[i][1]]
    item_info = market.get_list_items_info(list_hash_name=list_hash_name)
    print(names[i][1], item_info['data'][names[i][1]]['average'])
    time.sleep(0.21)

        

# Мой API ключ к маркету 42N05ro4gln24tP198b6A5F2Uu5h3ha