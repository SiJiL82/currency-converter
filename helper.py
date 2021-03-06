import pandas as pd
from colorama import init, Fore, Back, Style

init(autoreset=True)

# Colour Variables
green_text = Fore.GREEN + Back.RESET + Style.BRIGHT
white_text = Fore.RESET + Back.RESET + Style.NORMAL
blue_text = Fore.BLUE + Back.RESET + Style.BRIGHT


def get_max_dict_value_length(dict):
    """
    Returns the length of the longest value in a dictionary
    """
    # Initialise max to 0
    max = 0
    # For each key check if the length of the value is greater than current max
    for key in dict:
        if len(dict[key]) > max:
            max = len(dict[key])
    return max


def get_max_dict_key_length(dict):
    """
    Returns the length of the longest key in a dictionary
    """
    # Initialise max to 0
    max = 0
    # For each key check if the length of the key is greater than current max
    for key in dict:
        if len(key) > max:
            max = len(key)
    return max


def get_max_dict_subvalue_length(dict, key_name):
    """
    Returns the length of a the longest specified sub key in a dictionary
    """
    # Initialise max to 0
    max = 0
    # For each key check if length of specified sub key is greater than max
    for key in dict:
        length = len(dict.get(key)[key_name])
        if length > max:
            max = length
    return max


def get_csv_column(file_name, column_name):
    """
    Uses Pandas module to load a CSV and return a specified column as a list
    """
    # Open CSV
    csv = pd.read_csv(file_name)
    # Return array of the column specified
    return csv[column_name]


def add_csv_column(file_name, column_name, column_data):
    """
    Uses Pandas module to load a CSV, add a new column to the end
    and insert the supplied data
    """
    # Open CSV
    csv = pd.read_csv(file_name)
    #  Set new column data with header name specified
    csv[column_name] = column_data
    # Save new data to CSV
    save_csv(file_name, csv)


def save_csv(file_name, file):
    """
    Uses Pandas module to save a loaded CSV to file on disk
    """
    # Write CSV data out
    file.to_csv(file_name, index=False)


def compare_string_caseinsensitive(string1, string2):
    """
    Compare 2 strings with no case sensitivity
    """
    # Set both strings to lower case and compare.
    # Uses casefold rather than lower to support non-English chars
    if string1.casefold() == string2.casefold():
        return True
    else:
        return False


def check_csv_column_exists(file_name, column_name):
    """
    Uses Pandas module to open a CSV and check if supplied column exists
    """
    # Open CSV
    csv = pd.read_csv(file_name)
    if column_name in csv.columns:
        return True
    else:
        return False


def is_number(value):
    """
    Check if the supplied value (usually a string)
    can be converted to an int or float
    """
    # Try converting to a float
    try:
        float(value)
        return True
    except ValueError:
        # If that fails, try converting to an int
        try:
            int(value)
            return True
        except ValueError:
            # If that fails, this is not a number
            return False


def display_csv_header(file_name):
    """
    Use Pandas module to open a CSV and print the contents
    """
    # Open CSV
    csv = pd.read_csv(file_name)
    # Display just the header with the default 5 rows in table format
    # Excluding row numbers
    print(csv.head().to_markdown(index="never"))
