import json
import requests
import pprint

def get_api_key():
    with open("apikey.json") as apikey_file:
        data = json.load(apikey_file)
        return data["apikey"]

APIKEY = get_api_key()
currency_list = {}

def get_currency_list():
    url = f"http://api.exchangeratesapi.io/v1/symbols?access_key={APIKEY}"
    response = requests.request("GET", url)
    global currency_list
    currency_list = response.text

def display_currency_list():
    symbols = json.loads(currency_list)["symbols"]
    
    for symbol in symbols:
        print(f"{symbol}: {symbols.get(symbol)}")


get_currency_list()    
display_currency_list()
 