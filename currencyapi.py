import json

def get_api_key():
    with open("apikey.json") as apikey_file:
        data = json.load(apikey_file)
        return data["apikey"]

APIKEY = get_api_key()