"""
Import the entire gspread library, so we can access any function, class
or method within it
"""
import gspread
from google.oauth2.service_account import Credentials
# importing time module that will be used to delay some code execution
import time
# Create logo using pyfiglet
import pyfiglet

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('grace_bank')

customers = SHEET.worksheet('customers')

data = customers.get_all_values()

print(data)


def code_execution_delay(information):
    """
    Function to delay execution of some code and allow good
    flow of the program
    """
    print(information)
    time.sleep(1.5)


def welcome_to_gracebank():
    """
    Welcoming customers to Grace Bank Plc
    """
    gb_logo = pyfiglet.figlet_format("GRACE BANK Plc")
    print(gb_logo)
    print("Hi there! Welcome to Grace Bank Plc.\n")
    print("...the Bank of champions")
    code_execution_delay("press ANY button to start....\n")
    input("")
    code_execution_delay(
        "\nGBPlc-GBPlc-GBPlc------GBPlc-GBPlc-GBPlc-GBPlc"
        "------GBPlc-GBPlc-GBPlc------\n")


welcome_to_gracebank()
