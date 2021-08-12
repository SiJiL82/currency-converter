def get_max_dict_value_length(dict):
    """
    Returns the length of the longest value in a dictionary
    """
    max = 0
    for value in dict:
        if len(dict[value]) > max:
            max = len(value)
    return max