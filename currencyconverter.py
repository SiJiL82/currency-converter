import currencyapi as api
import helper
import os
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style


# Style the text for user prompts
prompt_style = Style.from_dict({
    # User input (default text).
    '': '#ffffff',
    # Prompt.
    'prompt_user': '#ffff00',
})


def press_enter_to_continue():
    """
    Loop until user presses Enter key,
    rather than jumping straight back to the menu.
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
    message = [
        ('class:prompt_user', prompt_text)
    ]
    while True:
        user_input = prompt(message,
                            style=prompt_style,
                            completer=key_completer)
        try:
            if api.check_currency_in_list(user_input):
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


def search_currencies():
    """
    Search the currency names and display all results that match
    provided search term
    """
    prompt_message = [
        ('class:prompt_user', "Enter search term, for example country name\n\
or common currency denomination (e.g.: 'Pound'): ")
    ]
    user_input = prompt(prompt_message, style=prompt_style)
    keylist = api.search_currency_name(user_input)
    print(f"{helper.blue_text}Matching results:")
    api.display_currency_list(keylist)
    press_enter_to_continue()


def view_exchange_rate():
    """
    Get the exchange rate for 2 currencies
    """
    source = prompt_for_currency("Enter source currency: ")
    destination = prompt_for_currency("Enter destination currency: ")
    exchange_rate = api.get_exchange_rate(source, destination)
    api.display_exchange_rate(source, destination, exchange_rate)
    press_enter_to_continue()


def convert_single_value():
    """
    Converts a single numerical value from one currency to another
    """
    source = prompt_for_currency("Enter source currency: ")
    destination = prompt_for_currency("Enter destination currency: ")
    exchange_rate = api.get_exchange_rate(source, destination)

    prompt_message = [
        ('class:prompt_user', "Enter value to convert: ")
    ]
    while True:
        user_input = prompt(prompt_message, style=prompt_style)
        try:
            if user_input.isdigit():
                convert_amount = float(user_input)
                break
            else:
                raise ValueError()
        except ValueError:
            print("Please enter a valid currency value to convert.")
    converted_amount = api.convert_currency(source,
                                            destination,
                                            convert_amount,
                                            exchange_rate)
    api.display_converted_currency(source,
                                   destination,
                                   convert_amount,
                                   converted_amount)
    press_enter_to_continue()


def convert_file_values():
    """
    Converts all values in a specified column in a file to a specified currency
    """
    # Prompt user to enter a path to a CSV file
    prompt_message = [
        ('class:prompt_user', "Enter the path to the CSV file containing \
the data you want to convert: ")
    ]
    while True:
        filename = prompt(prompt_message, style=prompt_style)
        # Check if user has pressed "q" to cancel and go back to the main menu
        if filename == "q":
            press_enter_to_continue()
        # Check if the file provided exists, and is a .csv
        try:
            extmatch = helper.compare_string_caseinsensitive(".csv",
                                                             os.path.splitext(
                                                                 filename)[1])
            if os.path.isfile(filename) and extmatch:
                break
            else:
                raise ValueError
        # Print error message if not
        except ValueError:
            print(f"{helper.blue_text}Please enter a valid file name, or \
{helper.white_text}q {helper.blue_text}to cancel")
    # Display the first 5 rows of the CSV before it's updated
    helper.display_csv(filename)
    # Prompt user to enter the column to convert
    prompt_message = [
        ('class:prompt_user', "Enter the column header containing \
the data you want to convert: ")
    ]
    while True:
        source_column_name = prompt(prompt_message, style=prompt_style)
        # Check if user has pressed "q" to cancel and go back to the main menu
        if source_column_name == "q":
            press_enter_to_continue()
        # Check if the column provided exists in the file
        try:
            if helper.check_csv_column_exists(filename, source_column_name):
                break
            else:
                raise ValueError
        # Print error message if not
        except ValueError:
            print(f"{helper.blue_text}Please enter a valid column name, or \
{helper.white_text}q {helper.blue_text}to cancel")
    # Check if the column provided is a currency name
    if api.check_currency_in_list(source_column_name.upper()):
        print(f"{helper.blue_text}Column name supplied matches currency: \
{helper.white_text}\
{api.currency_list_dict.get(source_column_name.upper())['currencyName']}.")
        print(f"{helper.blue_text}Do you wish to set the source currency to this value \
{helper.green_text}{source_column_name.upper()}{helper.blue_text}?\
{helper.white_text}")
        prompt_message = [
            ('class:prompt_user', "y/n: ")
        ]
        # If it is, check if user wants to use it as the source currency
        while True:
            user_input = prompt(prompt_message, style=prompt_style)
            try:
                if user_input.lower() == "y":
                    source = source_column_name.upper()
                    break
                elif user_input.lower() == "n":
                    break
                else:
                    raise ValueError
            except ValueError:
                print(f"{helper.blue_text}Please enter a valid response: ")
    # If not a valid currency, or user chose not to use it,
    # prompt for source currency.
    else:
        source = prompt_for_currency("Enter the source currency \
the data is stored in: ")
    # Prompt user for destination currency to convert to
    destination = prompt_for_currency("Enter the currency to convert to: ")
    # Get existing data from the CSV
    source_data = helper.get_csv_column(filename, source_column_name)
    # Get the exchange rate for the supplied currencies
    exchange_rate = api.get_exchange_rate(source, destination)
    # Convert the data
    print(f"{helper.blue_text}Writing converted data to file...\
{helper.white_text}")
    converted_data_arr = []
    for data in source_data:
        # Check the data is a number and can be converted
        if not helper.is_number(data):
            print(f"{helper.blue_text}Supplied data is not numerical. \
Aborting conversion.{helper.white_text}")
            # Go back to main menu.
            # Breaks out of the current code loop when the program is exited.
            press_enter_to_continue()
        # If data is a valid number,
        # convert it using the exchange rate already stored.
        converted_data = api.convert_currency(source,
                                              destination,
                                              data,
                                              exchange_rate)
        # Add the converted data to the array of new data
        converted_data_arr.append(converted_data)
    # Add the new column to the CSV and save it
    helper.add_csv_column(filename, destination, converted_data_arr)
    print(f"{helper.blue_text}File updated:{helper.white_text}")
    # Display the first 5 rows of the CSV after the update
    helper.display_csv(filename)
    # Return to main menu
    press_enter_to_continue()


# Menu options
options = [
    {
        "text": "List available currencies",
        "action": list_currencies
    },
    {
        "text": "Search for a currency",
        "action": search_currencies
    },
    {
        "text": "View an exchange rate",
        "action": view_exchange_rate
    },
    {
        "text": "Convert a single value to another currency",
        "action": convert_single_value
    },
    {
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
        print(f'{helper.green_text}{options.index(option) + 1}{helper.white_text}: \
{option.get("text")}')
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
            user_input = prompt(prompt_message, style=prompt_style)

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
            print(f"{helper.blue_text}Please enter a valid number value for \
one of the following options:")
            # Re-show the menu if a valid option wasn't shown
            menu()
    # If last option was chosen, quit
    if choice == len(options) + 1:
        print("Exiting.")
        raise SystemExit
    # Call the action for the option in the array position chosen
    options[choice-1]["action"]()


def ui():
    # Print welcome text to the user
    print(f"{helper.blue_text}Please enter the number value for one of the \
following options:{helper.white_text}")
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


main()
