import json
import requests
import helper 

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
    i = 1
    print_str = ""
    #max key length plus spacing, plus max value length, plus spacing
    column_width = helper.get_max_dict_key_length(symbols) + 2 + helper.get_max_dict_value_length(symbols) + 2
    for symbol in symbols:
        str = f"{symbol}: {symbols.get(symbol)}"
        if i == 4:
            print_str += "\n"
            i = 1
        print_str += f"{str: <{column_width}}"
        i += 1
    print(print_str)

get_currency_list()    
display_currency_list()
