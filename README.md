# Currency Converter

This project is a Python command line application that gives the user options to view and use currency conversion rates.

The application can be used in a web browser at [Heroku Deployment](https://currency-converter-sijil82.herokuapp.com/)

## Table of Contents
* [Design](#design)
    * [User Stories](#user-stories)
    * [Application Workflow](#application-workflow)
* [Features](#features)
    * [User Menu](#user-menu)
    * [Up to Date Data](#up-to-date-data)
    * [View All Currencies](#view-all-currencies)
    * [Search For A Currency](#search-for-a-currency)
    * [View a Currency Conversion Rate](#view-a-currency-conversion-rate)
    * [Convert a Single Value](#convert-a-single-value)
    * [Convert Values in File](#convert-values-in-file)
* [Testing](#testing)
    * [User Story Testing](#user-story-testing)
    * [Application Testing](#application-testing)
* [Validation](#validation)
* [Deployment](#deployment)
* [Credits](#credits)

# Design
## User Stories
-  __As a user of the application, I want to:__
    - Enter 2 currencies and see the exchange rate between them.  
        - Seeing the rate in both directions would be a bonus.  
    - Enter a source currency, a destination currency and a value, and have the value converted into the destination currency.  
        - See the exchange rate that was used for the calculation.  
    - Be sure any calculations I make are using the latest exchange data.  
    - Have an intuitive UI that makes it clear what operations I can perform.  
    - Be able to make calculations quickly, without having to type out the entire currency name.  
        - Being shown currency abbreviations would be a bonus, so I don't have to look them up.  
    - Have the ability to pass in a spreadsheet of data to be processed, rather than have to enter each calculation manually.  
## Application Workflow
Below is a high level overview of the workflow through the application.  
![Currency Converter Workflow](readme-assets/images/currency-converter-workflow.png)
# Features
- ## User Menu
    - Options presented to user allowing them to control the program flow.  
    - Created dynamically from an array of objects defining the actions, making it easy to expand.  
    - The "Quit" option is automatically appended to the end of the list.  
    - Colour formatting makes the menu clear to users.  
    - Validation ensures only numerical values from the list can be chosen.  
    ![Main Menu](readme-assets/images/user_menu.png)
- ## Up to Date Data
    - When the program is run, the latest list of currencies are pulled from the API automatically without the user needing to request them.  
    - All currency conversion data is pulled from the API as it is requested, ensuring data is as up to date as possible.  
- ## View All Currencies
    - Choosing option 1 on the menu will list all the available currencies.  
    - The 3 letter currency ID and full currency name are both displayed, with colour formatting to improve readability.   
    - The currency list is displayed in a dynamic column layout, where the number of columns automatically fits the size of the terminal the application is run in  
        - Default xTerm console (80 characters wide):  
        ![Currency List - xTerm](readme-assets/images/currency_list_xterm.png)
        - Default Windows 10 Terminal (120 characters wide):  
        ![Currency List - Windows 10 Terminal](readme-assets/images/currency_list_win10_term.png)
        - Windows 10 Terminal full screen (423 characters wide):  
        ![Currency List - Windows 10 Full Screen](readme-assets/images/currency_list_win10_term_full_screen.png)
- ## Search for a Currency
    - Prompts the user to enter a search term, and then returns all currencies where the currency name contains that term.
    - Case insensitive search, as the API returns some currencies with the first letter of a word capitalised, and others not:  
    ![Currency Search Case Insensitive](readme-assets/images/search_case_insensitive.png)
    - Allows the user to enter either the common currency term (e.g.: "Franc") or a country (e.g.: "Croatia") to find the relevant currency code:  
    ![Currency Search - Franc](readme-assets/images/search_results_franc.png)  
    ![Currency Search - Croatia](readme-assets/images/search_results_croatia.png)  
- ## View a Currency Conversion Rate
    - Prompts user for a source then destination currency to show an exchange rate for.  
    - User can start typing any 3 letter currency ID and the application will show an autocomplete prompt for currencies that match what they are typing.  
        - While all currency codes are uppercase, the user can enter text in lowercase or uppercase (but not mixed) to find currencies.
        - If lowercase is used, the application automatically converts it to uppercase.  
    ![Autocomplete Prompt For Currency](readme-assets/images/view_exchange_rate_autocomplete.png)  
    ![Autocomplete Prompt For Currency Lowercase](readme-assets/images/view_exchange_rate_complete_lowercase.png)  
    ![Currency Converted To Uppercase](readme-assets/images/currency_lower_to_upper.png)  
    - After choosing a currency code, the code and full currency name are shown to the user as confirmation.  
    ![Confirmation After Choosing Currency](readme-assets/images/view_exchange_rate_confirmation.png)  
    - After choosing both currencies, the application displays the currency conversion in both directions in a clear readable format.  
    ![View Exchange Rate](readme-assets/images/view_exchange_rate_completed.png)
- ## Convert a Single Value  
    - Prompts user for a source then destination currency, followed by a numerical amount to convert.  
    - User can again use the auto complete functionality to choose the currencies they wish to use.    
    - Displays the value entered converted to the destination currency in a user readable format.  
    ![Convert Single Value Results](readme-assets/images/convert_value_results.png)  
    - Converted value retains all decimal places from the calculation, so it can be used for an application where precise calculations are critical.  
- ## Convert Values in File  
    - Converts a specified column of data in a supplied Comma Separated Value (.csv) file to a destination currency, and appends the data in that currency to the file as a new column.  
    - Prompts the user for:  
        - A .CSV file to read.  
            - Displays the column headers and the first 5 rows of data to the user to assist with the following operations.  
            ![Prompt for CSV File](readme-assets/images/convert_file_filename.png)
            - The file path can be relative to the program directory (as above) or an absolute path in another location  
            ![Open Absolute File Path](readme-assets/images/convert_file_absolute_path.png)
        - A column in that file with data in to convert. 
            - If the column header matches a currency, asks the user if they wish to use that, rather than prompt for the currency in the next step.  
            ![Prompt For Column Name](readme-assets/images/convert_file_column_name_match.png) 
        - Source currency to convert from if not set from file.  
        ![Prompt For Source Currency](readme-assets/images/convert_file_select_column.png)
        - Destination currency to convert to.  
        ![Prompt For Destination Currency](readme-assets/images/convert_file_destination.png)
        - The data in the supplied column is converted to the destination currency, and the new data is appended to the file as a new column.  
            - The first 5 rows of data with the new column are shown to the user as confirmation that the operation has succeeded.  
            ![File Conversion Complete](readme-assets/images/convert_file_complete.png)
            - If the destination currency name matches an existing column name, the user is prompted to enter a new column name to use, to prevent data being overwritten.  
            ![New Column Name Specified](readme-assets/images/convert_file_new_column_name.png)
    - A sample `car_prices.csv` file is included with this project that can be used to test the process. Simply enter "car_prices.csv" as the file name when prompted.  
        - Source data:  
        ![File Conversion Before](readme-assets/images/file_conversion_before.png)
        - After column has been converted and new data saved to file:  
        ![File Conversion After](readme-assets/images/file_conversion_after.png)
# Testing
## User Story Testing
-  __User Features Requested:__
    - Request: Enter 2 currencies and see the exchange rate between them.  
        - Result: The user can choose the "View and exchange rate" option, enter their 2 currencies and be shown the exchange rate between these currencies.  
        - Request: Seeing the rate in both directions would be a bonus.  
            - Result: The application automatically returns the exchange rate for the chosen currencies in both directions.  
    - Request: Enter a source currency, a destination currency and a value, and have the value converted into the destination currency.  
        - Result: The user can choose the "Convert a single value to another currency" option, enter their currencies and a value to be converted and will be shown the converted amount.  
        - Request: See the exchange rate that was used for the calculation.  
            - Result: This was not implemented as it made the user experience feel cluttered. However the user can choose the "View an exchange rate" option to see the rate used for 2 currencies.
    - Request: Be sure any calculations I make are using the latest exchange data.  
        - Result: The application pulls the latest available data from the API each time a calculation is performed.
    - Request: Have an intuitive UI that makes it clear what operations I can perform.  
        - Result: The application has a clear menu and user prompts, with consistent colour formatting added to assist with presenting information to the user.  
    - Request: Be able to make calculations quickly, without having to type out the entire currency name.  
        - Result: The application uses only the 3 letter abbreviation for a currency for inputs by the user, making it quicker to enter chosen currencies.  
        - Request: Being shown currency abbreviations would be a bonus, so I don't have to look them up.  
            - Result: The user can choose the "List available currencies" option to present all available currencies with their full name and 3 letter abbreviation.  
    - Request: Have the ability to pass in a spreadsheet of data to be processed, rather than have to enter each calculation manually.  
        - Result: The user can choose the "Convert values from a supplied file to another currency" to load a CSV file with data they want to be converted.  
## Application Testing
- The menu input option checks for valid user input and prompts the user to input a valid choice if one is not entered:  
    - Invalid number chosen:  
    ![Invalid Menu Number Choice](readme-assets/images/testing_invalid_numerical_menu_choice.png)
    - Invalid alphabetical value entered:  
    ![Invalid Menu String Choice](readme-assets/images/testing_invalid_string_menu_choice.png)
- Searching for a currency where no results are found, or not entering a search term displays a message stating no results were found:  
![No Search Results Found](readme-assets/images/testing_no_search_results.png)
- Entering an input that doesn't match an available currency code prompts the user to enter a valid one:  
![Invalid Currency Code](readme-assets/images/testing_invalid_currency.png)
- Entering a non-numerical value to convert prompts the user to enter a valid value:  
![Invalid Value To Convert](readme-assets/images/testing_invalid_conversion_value.png)
- Entering a filename that doesn't exist when trying to convert a file's data prompts the user to enter a valid file:  
![Invalid File Path](readme-assets/images/testing_invalid_file.png)
- Entering a filename with an extension that isn't .csv prompts the user to enter a valid file:  
![Invalid File Extension](readme-assets/images/testing_invalid_extension.png)
- Providing a file to convert with data that isn't numerical will abort the conversion:  
![Invalid File Data](readme-assets/images/testing_invalid_file_data.png)
# Validation
All code has been run through the [PEP8](http://pep8online.com) online checker to validate the Python code.
No issues were found:
- currencyapi.py:  
![currencyapi.py PEP8 Check](readme-assets/images/currencyapi_pep8_check.png)
- currencyconverter.py:  
![currencyconverter.py PEP8 Check](readme-assets/images/currencyconverter_pep8_check.png)
- helper.py:  
![helper.py PEP8 Check](readme-assets/images/helper_pep8_check.png)
# Deployment
## Prerequisites:
- Generate an API Key at [Currency Converter API](https://free.currencyconverterapi.com/)
    - Both deployment methods below will require this API Key
## To deploy the project as an application that can be run locally:
- **Note:** This project requires you to have [Python](https://www.python.org/) installed on your local PC.
    - You will also need [pip](https://pip.pypa.io/en/stable/installation/) installed to allow installation of modules the application uses.  
- Create a local copy of the GitHub repository, by following one of the 2 processes below:
    - Download code:
        - Go to the [GitHub Repo](https://github.com/SiJiL82/currency-converter) page.
        - Click the `Code` button and download the ZIP file containing the project.
        - Extract the ZIP file to a location on your PC.
    - Clone the repository:
        - Open a terminal to the location you wish to run the application from.
        - Run the command `git clone https://github.com/SiJiL82/currency-converter.git`
- Install Python module dependencies:
    - Open a terminal to the folder you have copied the code to.
    - Run the command `pip install -r requirements.txt`
- In the folder you extracted the project files to, create an `env.py` file, and add the lines below:
    - `SERVER TYPE` should be replaced with the API key type you have chosen, from: `Free`, `Premium`, `Prepaid`  
```python
import os
os.environ.setdefault("APIKEY", "API KEY GENERATED ABOVE")
os.environ.setdefault("APITYPE", "SERVER TYPE")
```
- Open a terminal window to the location you extracted the files to, and run:  
`python currencyconverter.py`  
## To deploy the project to Heroku so it can be run as a remote web application:
- Clone the repository:
    - Open a terminal to the location you wish to run the application from.
    - Run the command `git clone https://github.com/SiJiL82/currency-converter.git`
- Create your own GitHub repository to host the code.
- Run the command `git remote set-url origin <Your GitHub Repo Path>` to set the remote repository location to your repository.
- Push the files to your repository with `git push`
- Create a [Heroku](https://www.heroku.com) account if you don't already have one.
- Create a new Heroku application
- Go to the Deploy tab:
    - Link your GitHub account.
    - Connect the application to the repository you created.
- Go to the Settings tab:
    - Click "Add buildpack"
        - Add the Python and Node.js buildpacks
        - Ensure that the Python buildpack is first in the list:  
        ![Heroku Buildpack Order](readme-assets/images/deploy_heroku_buildpacks.png)
    - Click "Reveal Config Vars"
        - Add 2 new Config Vars:
            - Key: `APIKEY` Value: `API Key generated earlier`
            - Key: `APITYPE` Value: `API Type chosen when generating key, from: 'Free', 'Premium', 'Prepaid'`
- Go back to the Deploy tab:
    - Click "Deploy Branch"
    - Monitor the build logs for completion of the deployment.
- Click "Open app" to launch the application inside a web page.  
# Credits
## The following resources were referenced during the development of this project:
- Colour formatting: [Colorama](https://pypi.org/project/colorama/)
    - Initial colour formatting not used in final build: [OzzMaker.com](https://ozzmaker.com/add-colour-to-text-in-python/)
- Auto complete prompting: [Python Prompt Toolkit](https://python-prompt-toolkit.readthedocs.io/en/master/pages/asking_for_input.html#asking-for-input)
- Exchange rates API: [CurrencyConverterAPI.com](https://free.currencyconverterapi.com/)
- CSV loading and manipulation: [Pandas Library](https://pandas.pydata.org/)
