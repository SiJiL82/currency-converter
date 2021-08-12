import json
import requests
import helper 

def get_api_key():
    """
    Load the API key from apikey.json and store in variable for later re-use
    """
    with open("apikey.json") as apikey_file:
        data = json.load(apikey_file)
        return data["apikey"]

#Store API key for use in other functions
APIKEY = get_api_key()

# Global variable to store curency list in
currency_list = {}
currency_list_dict = {}

def get_currency_list():
    """
    Pull the latest list of available currencies from the API
    """
    url = f"http://api.exchangeratesapi.io/v1/symbols?access_key={APIKEY}"
    response = requests.request("GET", url)
    # Store API result in the global variable for use in other functions
    # This is a string value that needs converting to be used
    global currency_list
    currency_list = response.text

def display_currency_list():
    """
    Prints the available currencies out in a user readable format
    """
    # Get just the symbol list from the currency list string
    global currency_list_dict
    currency_list_dict = json.loads(currency_list)["symbols"]
    # Counter for number of columns in printed string
    i = 1
    # Number of columns to print
    # TODO: See if we can get the console width, divide it by column_width and make this dynamic
    num_columns = 4
    # Empty string to start the printed list with
    print_str = ""
    # Width of each column to print. This is:
    # max key length + spacing + max value length + spacing + colour code escape values
    column_width = helper.get_max_dict_key_length(currency_list_dict) + 2 + helper.get_max_dict_value_length(currency_list_dict) + 2 + 20
    # Loop through each symbol to get out the key and value to print to console
    for currency in currency_list_dict:
        # String for each key and value, with colour formatting around the key
        str = f"\033[1;32;40m{currency}\033[0;37;40m: {currency_list_dict.get(currency)}"
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

# Debugging
get_currency_list()    
display_currency_list()
