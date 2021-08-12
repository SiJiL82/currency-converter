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
    Returns the length of the longest value in a dictionary
    """
    max = 0
    for key in dict:
        if len(key) > max:
            max = len(key)
    return max