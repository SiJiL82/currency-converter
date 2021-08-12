def list_currencies():
    print("Available currencies:")

def view_exchange_rate():
    print("Enter source currency:")
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

def menu():
    for option in options:
        print(f'{option.get("id")}: {option.get("text")}') 

menu()