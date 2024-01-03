import pandas as pd
import csv
import requests
from urllib.parse import quote
import time
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pandas as pd
import time
from csgo_market_api import CSGOMarket

# # Больше 5 запросов в секунду не отправлять! Иначе ключ удалится
#
# names = pd.read_csv("names.csv")
# names = names.values.tolist()
#
# market = CSGOMarket(api_key='42N05ro4gln24tP198b6A5F2Uu5h3ha')
#
# for i in range(len(names)):
#     list_hash_name = [names[i][0]]
#     item_info = market.get_list_items_info(list_hash_name=list_hash_name)
#     print(names[i][0], item_info['data'][names[i][0]]['average'])
#     time.sleep(0.21)

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = '1KhgnBVi5b9CFFYOUbvhBGPNw_tCXd_68rXNJ4iMFlBQ'


names = pd.read_csv("names.csv")
names = names.values.tolist()
not_readed_names = []

def get_steam_info(name, num):
    url = 'https://steamcommunity.com/market/priceoverview/?appid=730&currency=5&market_hash_name='
    hash_name = quote(name)
    url = url + hash_name
    html = requests.get(url)

    if html.json():
        if list(html.json().values())[0] != "false":
            return list(html.json().values())[1:]
        else:
            print('request false')
            while list(html.json().values())[0] == "false":
                html = requests.get(url)
    else:
        print('request error')
        not_readed_names.append([name, num])


def main(fr, to):
    if not fr:
        fr = 0
    if not to:
        to = len(names)-1
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())

    try:
        service = build('sheets', "v4", credentials=credentials)
        sheets = service.spreadsheets()

        for i in names[fr:to]:
            time.sleep(2)
            sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Data!A{i[0]+2}", valueInputOption='USER_ENTERED',
                                   body={"values": [[i[1]]]}).execute()

            sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Data!B{i[0]+2}:E{i[0]+2}", valueInputOption='USER_ENTERED',
                                   body={"values": []}).execute()


    except HttpError as error:
        print(error)


main(0, 0)

print(not_readed_names)