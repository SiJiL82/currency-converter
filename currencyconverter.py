import currencyapi as api
import helper
import os
import shutil
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style

# Style the text for user prompts
input_prompt_style = Style.from_dict({
    # User input (default text).
    '': '#ffffff',
    # Prompt.
    'prompt_user': '#ffff00',
})

def press_enter_to_continue():
    """
    Loop until user presses Enter key, rather than jumping straight back to the menu.
    Makes it easier for user to see text returned by their operation.
    """
    while True:
        input(f"{helper.blue_text}Press Enter to go back to the main menu.\n")
        break
    ui()

def prompt_for_currency(prompt_text):
    """
    Asks the user to choose a currency from the available list.
    """
    key_completer = WordCompleter(list(api.currency_list_dict.keys()))
    print(f"{helper.blue_text}Start typing to present list of currencies.")
    print(f"{helper.blue_text}Press <TAB> and <ENTER> to select a currency.")
    print(f"{helper.blue_text}Note that all currencies are in UPPERCASE.")
    prompt_message = [
        ('class:prompt_user', prompt_text)
    ]
    while True:
        user_input = prompt(prompt_message, style=input_prompt_style, completer=key_completer)
        try:
            if user_input in api.currency_list_dict.keys():
                return user_input
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid currency code.\n")
    

def list_currencies():
    """
    Display the list of available currencies in user readable format
    """
    print(f"{helper.blue_text}Available currencies: {helper.white_text}")
    api.display_currency_list()
    press_enter_to_continue()

def view_exchange_rate():
    """
    Get the exchange rate for 2 currencies
    """
    source_currency = prompt_for_currency("Enter source currency: ")
    destination_currency = prompt_for_currency("Enter destination currency: ")
    exchange_rate = api.get_exchange_rate(source_currency, destination_currency)
    api.display_exchange_rate(source_currency, destination_currency, exchange_rate)
    press_enter_to_continue()

def convert_single_value():
    """
    Converts a single numerical value from one currency to another
    """
    source_currency = prompt_for_currency("Enter source currency: ")
    destination_currency = prompt_for_currency("Enter destination currency: ")
    exchange_rate = api.get_exchange_rate(source_currency, destination_currency)

    prompt_message = [
        ('class:prompt_user', "Enter value to convert: ")
    ]
    while True:
        user_input = prompt(prompt_message, style=input_prompt_style)
        try:
            if user_input.isdigit():
                convert_value = float(user_input)
                break
            else:
                raise ValueError()
        except ValueError:
            print("Please enter a valid currency value to convert.")
    api.convert_currency(source_currency, destination_currency, convert_value, exchange_rate)
    press_enter_to_continue()

def convert_file_values():
    """
    Converts all values in a specified column in a file to a specified currency
    """
    print("Enter the file name:")
    #prompt for input
    print("Enter the source column to convert:")
    #prompt for input
    print("Enter the currency to convert to:")
    #prompt for input
    print("Enter the destination column to enter the new values into:")
    #prompt for input
    press_enter_to_continue()

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
    """
    Initialises the program
    """
    # Get the most recent currency list from the API
    api.get_currency_list()
    
def menu():
    """
    Displays all program options to the user
    """
    for option in options:
        print(f'{helper.green_text}{option.get("id")}{helper.white_text}: {option.get("text")}') 
    # Add a Quit option after all the others
    print(f'{helper.green_text}{len(options) + 1}{helper.white_text}: Quit') 

def user_menu_choice():
    """
    Prompt user to choose one of the program options.
    Loops until they exit.
    """
    while True:
        try:
            # Get the user input
            prompt_message = [
                ('class:prompt_user', "Choice: ")
            ]
            user_input = prompt(prompt_message, style=input_prompt_style)

            # Check if input is numerical
            if user_input.isdigit():
                choice = int(user_input)
            else:
                raise ValueError()
            # Check input is valid from the list of available options
            if 1 <= choice <= len(options) + 1:
                break
            raise ValueError()
        except ValueError:
            print(f"{helper.blue_text}Please enter a valid number value for one of the following options:")
            # Re-show the menu if a valid option wasn't shown
            menu()
    # If last option was chosen, quit            
    if choice == len(options) + 1:
        print("Exiting.")
        return
    # Compare the input against possible options to pick the one that was chosen
    chosen_option = None
    for option in options:
        if option["id"] == choice:
            chosen_option = option
            break
    # Call the action function of the chosen option
    chosen_option["action"]()

def ui():
    # Print welcome text to the user
    print(f"{helper.blue_text}Please enter the number value for one of the following options:{helper.white_text}")
    menu()
    user_menu_choice()

def main():
    """
    Main program call
    """
    # Clear the console before starting
    os.system('cls' if os.name == 'nt' else 'clear')
    init()
    print(f"{helper.blue_text}Welcome to the Currency Converter.")
    ui()

#print(shutil.get_terminal_size())
#columns = 80, lines = 24
main()    