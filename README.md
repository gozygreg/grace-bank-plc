# GRACE BANK PLC (GBPlc)

## About the GBPlc

<img width="760" alt="GB Welcome page" src="https://user-images.githubusercontent.com/69070044/178149451-002d4e4a-d2f9-4a8a-8923-af86984a04d3.png">

## Table of Contents
* [UX](#UX)
* [Design](#Design)
* [Features](#Features)
* [Testing](#Testing)
* [Technologies](#Technologies)
* [Deployment](#Deployment)
* [Libraries](#Libraries)
* [Acknowledgement](#Acknowledgement)

## Features

## Design
### Wireframe
[Lucid app](https://www.lucidchart.com/) was used to plan the logic for this project. Below is a screenshot of the logic.

![Customer insights](https://user-images.githubusercontent.com/69070044/178149426-3586b790-93d9-4ee1-ab26-98f57e9085bd.png)

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
