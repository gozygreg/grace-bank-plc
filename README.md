# GRACE BANK PLC (GBPlc)

## About the GBPlc
Grace Bank Plc (GBPlc) is a banking application that allows customers to perform basic banking operation such as deposting and withdrawal of funds as well as checking their account balance. The unique properties of the (GBPlc) app is that it allows customers to still withdraw funds even if they do not have enough funds in their account balance. It however does inform customers that they have gone in to an unarranged overdraft when this occurs.

<img width="760" alt="GB Welcome page" src="https://user-images.githubusercontent.com/69070044/178149451-002d4e4a-d2f9-4a8a-8923-af86984a04d3.png">

## Table of Contents
* [UX](#UX)
* [Design](#Design)
* [Features](#Features)
* [Data Base](#Googlesheet)
* [Testing](#Testing)
* [Technologies](#Technologies)
* [Deployment](#Deployment)
* [Libraries](#Libraries)
* [Acknowledgement](#Acknowledgement)

## Design
### Wireframe
[Lucid app](https://www.lucidchart.com/) was used to plan the logic for this project. Below is a screenshot of the logic.

![Customer insights](https://user-images.githubusercontent.com/69070044/178149426-3586b790-93d9-4ee1-ab26-98f57e9085bd.png)

## Features
### Welcome to GBPlc
The first things customers see on the able is the bank logo, a welcome message, the bank motto and then instruction on action need to take to proceed.

### New Customer (Register)/Existing Customer
Customers are to type an account name of their choice while the app searches for their name on google sheet. Existing customers are welcomed and navigated to the bank main menu while new customers are promted to registered by typing any key on their device. Thus their account name will be added onto the data base (googlesheet)
<img width="1273" alt="existing customer" src="https://user-images.githubusercontent.com/69070044/178149456-587a0750-9b4f-4522-b5fa-cff866c44009.png">

<img width="1270" alt="Register New customer:Menu" src="https://user-images.githubusercontent.com/69070044/178149484-ac838c4e-db85-43b6-b42f-7a813cc8c960.png">

### Account Name Validation
Customers are asked to try again if they fail to provide valid account name. The rule that have been set fot this app is that a valid account name must comprise of atleast a number e.g 'John1' is a valid name while 'John' is not valid.
<img width="1270" alt="account_name validation" src="https://user-images.githubusercontent.com/69070044/178149472-211744c2-00fd-4afb-a6e2-26ce52909096.png">

### Main Menu
The app has 4 basic function with corresponding 4 menu options to choose from. An error is raised if customer choose an option other than the 4 options provided. The options are D, W, B, E which are deposit, withdrawal, check balance and exit bank repectively.
<img width="1277" alt="Raising errors" src="https://user-images.githubusercontent.com/69070044/178149478-5a13aee4-8229-4c30-9a48-8ee1d77252c4.png">

 ### Deposit
 Customers are able to deposit funds by chosing 'd' or 'D' from the main menu options. The amount typed is stored on googlesheet and customer balance is updated.
 <img width="1266" alt="Deposit" src="https://user-images.githubusercontent.com/69070044/178149462-b1177919-d6b5-44ee-9946-00fa712aae60.png">

 ### Withdrawal
 Customers are able to withdraw funds even when their account balance is less than the requested withdrawal amount. Customers are informed that they are going into an overdraft if this is the case.
 <img width="1271" alt="withdraw" src="https://user-images.githubusercontent.com/69070044/178149465-e6f7da6b-213e-4a13-993c-8d36b1d85981.png">

### Checking account balance
Customers are able to check the amount they have in the their account by chosing 'b' or 'B' from the main menu.

### Exiting the bank
When customers complete their transactions, they can exit the bank by choosing 'e' or 'E' to end program

<img width="1280" alt="balance   exit" src="https://user-images.githubusercontent.com/69070044/178149482-42e08de4-fdfb-4b63-8a73-2b20feaf03b2.png">

## Testing
The code for this project was tested using [PEP8](http://pep8online.com/)
<img width="1209" alt="PEP8 Validator test" src="https://user-images.githubusercontent.com/69070044/178151965-007e26ee-b15d-4ecb-9663-62236ded1b0f.png">

## Deployment
This app was deployed to Heroku. Below are the steps taken for its deployment
- Create and account and log in to heroku
- Create a new app
- Go to settings option
- Add 'key/value' pairs. First key is CREDS and its value is copied from creds.json file on gitpod. The second key is PORT with 8000 as its value
- Add build pack. Add python first and then nodejs second in that order.
- Go to the top of the page, then select 'deploy tab' and then choose 'Github deployment'.
- [Click to nnavigate to the deployed project](https://grace-bank.herokuapp.com/) 

To clone the project, navigate to the repository button on the [GitHub](https://github.com/gozygreg/grace-bank-plc) and select zip or open with Github desktop. After that, copy and paste the link to your git terminal by clicking GitHub CLI and the copy button in the code dropdown menu.

## Libraries
The following libraries were utilised in building this project
* [Gspread](https://docs.gspread.org/en/v3.7.0/api.html)
* [Credentials](https://pypi.org/project/credentials/)
* [Time/sleep](https://www.programiz.com/python-programming/time/sleep)
* [Pyfiglet:](https://pypi.org/project/pyfiglet/0.7/) which was used to create the bank logo

## Acknowledgement
[Lucid app](https://www.lucidchart.com/) was used to plan the logic for this project. Below is a screenshot of the logic.
