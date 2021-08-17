import pandas as pd

# Colour Variables
green_text = "\033[1;32;40m"
white_text = "\033[0;37;40m"
blue_text = "\033[1;34;40m"

def get_max_dict_value_length(dict):
    """
    Returns the length of the longest value in a dictionary
    """
    max = 0
    for key in dict:
        if len(dict[key]) > max:
            max = len(dict[key])
    return max

def get_max_dict_key_length(dict):
    """
    Returns the length of the longest key in a dictionary
    """
    max = 0
    for key in dict:
        if len(key) > max:
            max = len(key)
    return max

def get_max_dict_subvalue_length(dict, key_name):
    """
    Returns the length of a the longest specified sub key in a dictionary
    """
    max = 0
    for key in dict:
        length = len(dict.get(key)[key_name])
        if length > max:
            max = length
    return max

def get_csv_column(file_name, column_name):
    """
    Uses Pandas module to load a CSV and return a specified column as a list
    """
    csv = pd.read_csv(file_name)
    return csv[column_name]

def add_csv_column(file_name, column_name, column_data):
    """
    Uses Pandas module to load a CSV, add a new column to the end and insert the supplied data
    """
    csv = pd.read_csv(file_name)
    csv[column_name] = column_data
    save_csv(file_name, csv)

def save_csv(file_name, file):
    """
    Uses Pandas module to save a loaded CSV to file on disk
    """
    file.to_csv(file_name, index=False)