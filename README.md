# **GRACE BANK PLC (GBPlc)**

## **About the GBPlc**
Grace Bank Plc (GBPlc) is a banking application that allows customers to perform basic banking operation such as deposting and withdrawal of funds as well as checking their account balance. The unique property of the (GBPlc) app is that it allows customers to still withdraw money even if they do not have enough funds in their account balance. It does, however, inform customers that they have gone in to an unarranged overdraft when this occurs.

<img width="760" alt="GB Welcome page" src="https://user-images.githubusercontent.com/69070044/178149451-002d4e4a-d2f9-4a8a-8923-af86984a04d3.png">

## **Table of Contents**
- [Design](#Design)
- [Features](#Features)
- [Data Base](#Googlesheet)
- [Testing](#Testing)
- [Unfixed-bug](#Unfixed bug)
- [Technologies used](#Technologies-used)
- [Deployment](#Deployment)
- [Libraries](#Libraries)
- [Acknowledgement](#Acknowledgement)

## **Design**
### Wireframe

[Lucid app](https://www.lucidchart.com/) was used to plan the logic for this project. Below is a screenshot of the logic.

![Customer insights](https://user-images.githubusercontent.com/69070044/178149426-3586b790-93d9-4ee1-ab26-98f57e9085bd.png)

## **Features**
### Welcome to GBPlc
The first things customers see on the able is the bank logo, a welcome message, the bank motto and then instruction on action needed to take to proceed.

### New Customer (Register)/Existing Customer
Customers are to type an account name of their choice while the app searches for their name on google sheet. Existing customers are welcomed and navigated to the bank main menu while new customers are promted to registered by typing any key on their device. Thus their account name will be added onto the data base (googlesheet)

<img width="1273" alt="existing customer" src="https://user-images.githubusercontent.com/69070044/178149456-587a0750-9b4f-4522-b5fa-cff866c44009.png">

<img width="1270" alt="Register New customer:Menu" src="https://user-images.githubusercontent.com/69070044/178149484-ac838c4e-db85-43b6-b42f-7a813cc8c960.png">

### Account Name Validation

Customers are asked to try again if they fail to provide a valid account name. A valid account name must comprise of atleast a number e.g 'John1' is a valid name while 'John' is not valid.

<img width="1270" alt="account_name validation" src="https://user-images.githubusercontent.com/69070044/178149472-211744c2-00fd-4afb-a6e2-26ce52909096.png">

### Main Menu
The app has 4 basic function with corresponding 4 menu options to choose from. An error is raised if customer choose an option other than the 4 options provided. The options are D, W, B, E which are deposit, withdrawal, check balance and exit bank repectively.

<img width="1277" alt="Raising errors" src="https://user-images.githubusercontent.com/69070044/178149478-5a13aee4-8229-4c30-9a48-8ee1d77252c4.png">

 ### Deposit
 Customers are able to deposit funds by chosing 'd' or 'D' from the main menu options. The amount typed is stored on googlesheet and customer balance is updated.

 <img width="1266" alt="Deposit" src="https://user-images.githubusercontent.com/69070044/178149462-b1177919-d6b5-44ee-9946-00fa712aae60.png">

 ### Withdrawal
 Customers are able to withdraw funds by choosing 'w' or 'W' for the main menu

 <img width="1271" alt="withdraw" src="https://user-images.githubusercontent.com/69070044/178149465-e6f7da6b-213e-4a13-993c-8d36b1d85981.png">

 ### Overdraft
Customers are also able to withdraw funds even when their account balance is less than the requested withdrawal amount. Customers are informed that they are going into an overdraft if this is the case.

<img width="1274" alt="overdraft" src="https://user-images.githubusercontent.com/69070044/178153974-5283096a-1f4f-441a-a63b-61fa72cad9d8.png">

### Checking account balance
Customers are able to check the amount they have in the their account by chosing 'b' or 'B' from the main menu.

### Exiting the bank
When customers complete their transactions, they can exit the bank by choosing 'e' or 'E' to end program

<img width="1280" alt="balance   exit" src="https://user-images.githubusercontent.com/69070044/178149482-42e08de4-fdfb-4b63-8a73-2b20feaf03b2.png">

### Data Base
Google Sheet API was utilised to store customer transactions. It keeps track of the customer deposits, withdrawals and also read customer balance when its requested by the customer.

<img width="1217" alt="Google sheet" src="https://user-images.githubusercontent.com/69070044/178165643-5fe9e256-ba61-47d4-a780-4cedacbf0180.png"> 

## **Testing**
The code for this project was tested using [PEP8](http://pep8online.com/)

<img width="1209" alt="PEP8 Validator test" src="https://user-images.githubusercontent.com/69070044/178151965-007e26ee-b15d-4ecb-9663-62236ded1b0f.png">

## **Unfixed Bug and planned improvements**
An error arises when an old customer log in again and try to deposit funds. I encountered this late and close to submittion deadline. I plan to resolve this as well as create an overdraft limit such that if customer go above this limit, they will be charged an interest of 2%.
## **Technologies Used**
- [Python](https://www.python.org/)
- [Heroku](https://id.heroku.com/login)
- [GitPod](https://www.gitpod.io/)
- [GitHub](https://github.com/)

## **Deployment**
This app was deployed to Heroku. Below are the steps taken for its deployment
- Create and account and log in to heroku
- Create a new app
- Go to settings option
- Add 'key/value' pairs. First key is CREDS and its value is copied from creds.json file on gitpod. The second key is PORT with 8000 as its value
- Add build pack. Add python first and then nodejs second in that order.
- Go to the top of the page, then select 'deploy tab' and then choose 'Github deployment'.
- [Click to navigate to the deployed project](https://grace-bank.herokuapp.com/) 

To clone the project, navigate to the repository button on the [GitHub](https://github.com/gozygreg/grace-bank-plc) and select zip or open with Github desktop. After that, copy and paste the link to your git terminal by clicking GitHub CLI and the copy button in the code dropdown menu.

## **Libraries**
The following libraries were utilised in building this project
* [Gspread](https://docs.gspread.org/en/v3.7.0/api.html) to enable the opening, accessing and reading of googlesheet data
* [Credentials](https://pypi.org/project/credentials/) they serve as unique identifiers required to access my API
* [Time/sleep](https://www.programiz.com/python-programming/time/sleep) was used to create a timely flow of event as customer perform transactiond
* [Pyfiglet](https://pypi.org/project/pyfiglet/0.7/) was used to create the bank logo

## **Acknowledgement**
- Code institute love sandwiches project was quit instrumental in helping me build this app. I was able to follow the example to help me incooporate google API
- A big thank you goes to my mentor, Martina Terlevic for her continious support.
- I also appreciate my fellow [code institute](https://codeinstitute.net/) students in the [slack community](https://slack.com/intl/en-gb/) for their help and ideas
- I acknowledge the following online tutorials as they were very helpful
  - [Bank management system project by Adones Evangelista](https://itsourcecode.com/free-projects/python-projects/bank-management-system-project-in-python-with-source-code/)
  - [How to create a banking system using Object oriented Programming in python for beginners by Johan Godinho](https://www.youtube.com/watch?v=xTh-ln2XhgU)
  - [w3schools](https://www.w3schools.com/) has been a go-to website for answers during the building of this project.
- [Lucid app](https://www.lucidchart.com/) was used to plan the logic for this project. Below is a screenshot of the logic.
- I also appreciate my wife Grace; who this project after was named after.

*[Back to top](#grace-bank-plc-gbplc)*