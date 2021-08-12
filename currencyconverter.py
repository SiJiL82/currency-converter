import currencyapi as api
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

def prompt_for_currency(prompt_text):
    """
    Asks the user to choose a currency from the available list.
    """
    key_completer = WordCompleter(list(api.currency_list_dict.keys()))
    print("Start typing to present list of currencies.")
    print("Press <TAB> and <ENTER> to select a currency")
    user_input = prompt(prompt_text, completer=key_completer)
    print(f"Key chosen: {user_input}")

def list_currencies():
    print("Available currencies:")
    api.display_currency_list()

def view_exchange_rate():
    prompt_for_currency("Enter source currency:")
    #prompt for input
    print("Enter destination currency:")
    #prompt for input

def convert_single_value():
    print("Enter source currency:")
    #prompt for input
    print("Enter destination currency:")
    #prompt for input
    print("Enter value to convert:")
    #prompt for input

def convert_file_values():
    print("Enter the file name:")
    #prompt for input
    print("Enter the source column to convert:")
    #prompt for input
    print("Enter the currency to convert to:")
    #prompt for input
    print("Enter the destination column to enter the new values into:")
    #prompt for input

options = [
    {
        "id": 1,
        "text": "List available currencies",
        "action": list_currencies
    },
    {
        "id": 2,
        "text": "View an exchange rate",
        "action": view_exchange_rate
    },
    {
        "id": 3,
        "text": "Convert a single value to another currency",
        "action": convert_single_value
    },
    {
        "id": 4,
        "text": "Convert values from a supplied file to another currency",
        "action": convert_file_values
    }
]

def init():
    api.get_currency_list()
    print("Welcome to the Currency Converter.")
    print("Please enter the number value for one of the following options:")

def menu():
    for option in options:
        print(f'{option.get("id")}: {option.get("text")}') 

def user_menu_choice():
    while True:
        try:
            input_str = input("Choice: ")
            if input_str.isdigit():
                choice = int(input_str)
            else:
                raise ValueError()
            if 1 <= choice <= len(options):
                break
            raise ValueError()
        except ValueError:
            print("Please enter a valid number value for one of the following options:")
            menu()
    chosen_option = None
    for option in options:
        if option["id"] == choice:
            chosen_option = option
            break
    chosen_option["action"]()

        
init()
menu()
user_menu_choice()