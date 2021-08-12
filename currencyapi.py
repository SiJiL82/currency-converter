import json
import requests

def get_api_key():
    with open("apikey.json") as apikey_file:
        data = json.load(apikey_file)
        return data["apikey"]

APIKEY = get_api_key()

def get_currency_list():
    url = f"http://api.exchangeratesapi.io/v1/symbols?access_key={APIKEY}"
    response = requests.request("GET", url)
    return response.text
  