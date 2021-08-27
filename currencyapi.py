import json
import requests
import helper
import os
import shutil
import math
if os.path.exists("env.py"):
    import env

# Store API key for use in other functions
APIKEY = os.environ.get("APIKEY")
APITYPE = os.environ.get("APITYPE")

# Global variable to store curency list in
currency_list_dict = {}

# Global variable for API base URL
api_type_switcher = {
    "Free": "free",
    "Premium": "api",
    "Prepaid": "prepaid"
}
url_prefix = api_type_switcher.get(APITYPE)
api_url = f"https://{url_prefix}.currconv.com/api/v7"


def get_currency_list():
    """
    Pull the latest list of available currencies from the API
    """
    url = f"{api_url}/currencies?apiKey={APIKEY}"
    response = requests.request("GET", url)
    # Store API result in the global variable for use in other functions
    try:
        global currency_list_dict
        currency_list_dict = json.loads(response.text)["results"]
    except Exception as e:
        print("Error:")
        print(e)


def search_currency_name(search_term):
    """
    Searches the currency name field of the API results
    Returns a list of the matching currency keys
    """
    # Array to store return values
    matched_keys = []
    # Loop through currencies, if name contains search term
    # add the currency key to return list
    if search_term != "":
        for key in currency_list_dict:
            if search_term.lower() in \
               currency_list_dict.get(key)['currencyName'].lower():
                matched_keys.append(key)
    return matched_keys


def display_currency_list(keylist=None):
    """
    Prints the available currencies out in a user readable format
    """
    if keylist is not None:
        currency_display_list = {key: currency_list_dict[key]
                                 for key in keylist}
    else:
        currency_display_list = currency_list_dict
    # Counter for number of columns in printed string
    i = 1

    # Width of each column to print. This is:
    # max key length + spacing + max value length
    # + spacing + colour code escape values
    value_length = helper.get_max_dict_subvalue_length(currency_display_list,
                                                       "currencyName")
    key_length = helper.get_max_dict_value_length(currency_display_list)
    colour_format_length = 20
    column_width = value_length + 2 + key_length + 2 + colour_format_length

    # Number of columns to print
    terminal_columns, terminal_rows = shutil.get_terminal_size()
    num_columns = math.floor(terminal_columns /
                             (column_width - colour_format_length))

    # Empty string to start the printed list with
    print_str = ""
    # Loop through each symbol to get out the key and value to print to console
    for currency in sorted(currency_display_list):
        # String for each key and value, with colour formatting around the key
        str = f"{helper.green_text}{currency}{helper.white_text}: \
{currency_display_list.get(currency)['currencyName']}"
        # If we've appended as many strings as there are columns,
        # reset the columns and start a new line
        if i > num_columns:
            print_str += "\n"
            i = 1
        # Add the key/value pair string to the overall string,
        # with the column width formatting
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
    url = f"{api_url}/convert?q={lookup},{reverse_lookup}\
&compact=ultra&apiKey={APIKEY}"
    # Get the API response
    response = requests.request("GET", url)
    exchange_rate = json.loads(response.text)
    return exchange_rate


def display_exchange_rate(source, destination, exchange_rate):
    """
    Displays the exchange rate from the API in a user readable format
    """
    # Set key for provided search
    lookup = f"{source}_{destination}"
    # Set key for reverse of search
    reverse_lookup = f"{destination}_{source}"
    # Get currency symbols for source and destination currencies
    source_currency_symbol = get_currency_symbol(source)
    destination_currency_symbol = get_currency_symbol(destination)
    # Display provided search result to user
    print(f"{helper.white_text}{source_currency_symbol}1 {helper.green_text}{source}\
{helper.white_text} is equal to {destination_currency_symbol}\
{exchange_rate.get(lookup)} {helper.green_text}{destination}\
{helper.white_text}")
    # Display reverse of search to user
    print(f"{destination_currency_symbol}1 {helper.green_text}{destination}\
{helper.white_text} is equal to {source_currency_symbol}\
{exchange_rate.get(reverse_lookup)} {helper.green_text}{source}\
{helper.white_text}")


def convert_currency(source, destination, amount, exchange_rate):
    """
    Converts the supplied amount to the destination currency
    """
    # Set key for the provided search
    lookup = f"{source}_{destination}"
    # Get the searched exchange rate from the passed in rates
    rate = exchange_rate.get(lookup)
    # Calculate the exchanged value
    amount_destination = amount * rate
    return amount_destination


def display_converted_currency(source, destination, amount, amount_converted):
    """
    Displays the converted currency results in a user readable format
    """
    # Get currency symbols for source and destination currencies
    source_currency_symbol = get_currency_symbol(source)
    destination_currency_symbol = get_currency_symbol(destination)
    # Display to user
    print(f"{helper.white_text}{source_currency_symbol}{amount} \
{helper.green_text}{source}{helper.white_text} = {destination_currency_symbol}\
{amount_converted} {helper.green_text}{destination}{helper.white_text}")


def get_currency_symbol(key):
    """
    Returns the currency symbol for a currency if it exists.
    Returns empty string if not.
    """
    if "currencySymbol" in currency_list_dict.get(key):
        return currency_list_dict.get(key)["currencySymbol"]
    else:
        return ""


def check_currency_in_list(key):
    """
    Checks if supplied currency exists in the API currency list
    """
    if key in currency_list_dict.keys():
        return True
    else:
        return False
