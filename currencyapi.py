import json
import requests
import helper
import os
if os.path.exists("env.py"):
    import env

#Store API key for use in other functions
APIKEY = os.environ.get("APIKEY")

# Global variable to store curency list in
currency_list_dict = {}

def get_currency_list():
    """
    Pull the latest list of available currencies from the API
    """
    url = f"https://free.currconv.com/api/v7/currencies?apiKey={APIKEY}"
    response = requests.request("GET", url)
    # Store API result in the global variable for use in other functions
    global currency_list_dict
    currency_list_dict = json.loads(response.text)["results"]

def display_currency_list():
    """
    Prints the available currencies out in a user readable format
    """   
    # Counter for number of columns in printed string
    i = 1
    # Number of columns to print
    # TODO: See if we can get the console width, divide it by column_width and make this dynamic
    num_columns = 3
    # Empty string to start the printed list with
    print_str = ""
    # Width of each column to print. This is:
    # max key length + spacing + max value length + spacing + colour code escape values
    column_width = helper.get_max_dict_subvalue_length(currency_list_dict, "currencyName") + 2 + helper.get_max_dict_value_length(currency_list_dict) + 2 + 20
    # Loop through each symbol to get out the key and value to print to console
    for currency in currency_list_dict:
        # String for each key and value, with colour formatting around the key
        str = f"{helper.green_text}{currency}{helper.white_text}: {currency_list_dict.get(currency)['currencyName']}"
        # If we've appended as many strings as there are columns, reset the columns and start a new line
        if i > num_columns:
            print_str += "\n"
            i = 1
        # Add the key/value pair string to the overall string, with the column width formatting
        print_str += f"{str: <{column_width}}"
        # Increment column counter
        i += 1
    # Display the end string to the console.
    print(f"{print_str}")

def get_exchange_rate(source, destination):
    """
    Displays the exchange rate for the passed in currencies
    """
    # Set string for provided search
    lookup = f"{source}_{destination}"
    # Set string for reverse of search
    reverse_lookup = f"{destination}_{source}"
    # Set API request URL
    url = f"https://free.currconv.com/api/v7/convert?q={lookup},{reverse_lookup}&compact=ultra&apiKey={APIKEY}"
    # Get the API response
    response = requests.request("GET", url)
    exchange_rate = json.loads(response.text)
    return exchange_rate

def display_exchange_rate(source, destination, exchange_rate):
    """
    Displays the exchange rate from the API in a user readable format
    """
    # Set string for provided search
    lookup = f"{source}_{destination}"
    # Set string for reverse of search
    reverse_lookup = f"{destination}_{source}"
    # Display provided search result to user
    print(f"1 {helper.green_text}{source}{helper.white_text} is equal to {exchange_rate.get(lookup)} {helper.green_text}{destination}{helper.white_text}")
    # Display reverse of search to user
    print(f"1 {helper.green_text}{destination}{helper.white_text} is equal to {exchange_rate.get(reverse_lookup)} {helper.green_text}{source}{helper.white_text}")

# Debugging
# get_currency_list()    
# display_currency_list()
