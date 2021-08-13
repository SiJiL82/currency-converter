import currencyapi as api
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

def prompt_for_currency(prompt_text):
    """
    Asks the user to choose a currency from the available list.
    """
    key_completer = WordCompleter(list(api.currency_list_dict.keys()))
    print("\033[1;34;40mStart typing to present list of currencies.")
    print("\033[1;34;40mPress <TAB> and <ENTER> to select a currency.")
    print("\033[1;34;40mNote that all currencies are in UPPERCASE.")
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
    print("\033[1;34;40mAvailable currencies: \033[0;37;40m")
    api.display_currency_list()

def view_exchange_rate():
    """
    Get the exchange rate for 2 currencies
    """
    source_currency = prompt_for_currency("Enter source currency: ")
    destination_currency = prompt_for_currency("Enter destination currency: ")
    exchange_rate = api.get_exchange_rate(source_currency, destination_currency)
    api.display_exchange_rate(source_currency, destination_currency, exchange_rate)

def convert_single_value():
    """
    Converts a single numerical value from one currency to another
    """
    print("Enter source currency:")
    #prompt for input
    print("Enter destination currency:")
    #prompt for input
    print("Enter value to convert:")
    #prompt for input

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
    # Print welcome text to the user
    print("\033[1;34;40mWelcome to the Currency Converter.")
    print("\033[1;34;40mPlease enter the number value for one of the following options:")
    # Reset console colour to white
    print("\033[0;37;40m")

def menu():
    """
    Displays all program options to the user
    """
    for option in options:
        print(f'\033[1;32;40m{option.get("id")}\033[0;37;40m: {option.get("text")}') 
    # Add a Quit option after all the others
    print(f'\033[1;32;40m{len(options) + 1}\033[0;37;40m: Quit') 

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
            print("Please enter a valid number value for one of the following options:")
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

def main():
    """
    Main program call
    """
    init()
    menu()
    user_menu_choice()

main()    