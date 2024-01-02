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

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = '1KhgnBVi5b9CFFYOUbvhBGPNw_tCXd_68rXNJ4iMFlBQ'

with open('names.csv', newline='') as f:
    reader = csv.reader(f)
    names = list(reader)
names.pop(0)
n=0
for i in names:
    names[n] = i[0]
    n += 1
print(names)
def main():
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

        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="Data!A1:C3").execute()

        values = result.get('values', [])

        sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Data!A1:A20", valueInputOption='USER_ENTERED',
                                body={"values": [names]}).execute()

        sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Data!B2:E2", valueInputOption='USER_ENTERED',
                               body={"values": [['done', 'done', 'done', 'done']]}).execute()

        for row in values:
            print(values)
    except HttpError as error:
        print(error)


main()

tp_info_list = []


def get_info():
    url = 'https://steamcommunity.com/market/priceoverview/?appid=730&currency=5&market_hash_name='

    with open('names.csv', newline='') as f:
        reader = csv.reader(f)
        names = list(reader)
    names.pop(0)

    for i in names:
        time.sleep(0.2)
        url = 'https://steamcommunity.com/market/priceoverview/?appid=730&currency=5&market_hash_name='
        hash_name = quote(str(i[0]))
        url = url + hash_name
        html = requests.get(url)

        if html.json():
            if list(html.json().values())[0] != "false":
                tp_info_list.append(list(html.json().values())[1:])
                print(list(html.json().values())[1:])


# get_info()
# print(tp_info_list)
