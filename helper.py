# Colour Variables
green_text = "\033[1;32;40m"
white_text = "\033[0;37;40m"

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