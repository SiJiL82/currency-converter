# Currency Converter

This project is a Python command line application that can convert numerical values between different currencies.  

The application can be used in a web browser at [LINK]  

## Table of Contents
* [Design](#design)
    * [User Stories](#user-stories)
    * [Application Workflow](#application-workflow)
* [Features](#features)
* [Testing](#testing)
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
# Testing

# Deployment

# Credits
https://ozzmaker.com/add-colour-to-text-in-python/
https://python-prompt-toolkit.readthedocs.io/en/master/pages/asking_for_input.html#asking-for-input
https://free.currencyconverterapi.com/