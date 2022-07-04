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

# customers = SHEET.worksheet('customers')

# data = customers.get_all_values()

# print(data)


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
    code_execution_delay("\npress ANY button to start....\n")
    input("")
    code_execution_delay(
        "\nGBPlc-GBPlc-GBPlc------GBPlc-GBPlc-GBPlc-GBPlc"
        "------GBPlc-GBPlc-GBPlc------\n")


def validate_data(menu_choice):
    """
    Function to ensure customers input the right data
    and to prevent app from breaking.
    """
    try:
        if menu_choice != "d" or menu_choice != "w" or \
             menu_choice != "b" or menu_choice != "e":
            print("Invalid choice, Try again")
    except ValueError:
        print("Invalid choice: Only letters d,w,b,e allowed")


def login():
    """
    Customer login their account name which will be verified
    """
    while True:
        account_name = input(
            "Enter your account name below. "
            "\nIf you are new customers, create an account name "
            "which should have atleast one number. \n"
        ).lower()

        if account_name.isalpha():
            print(
                "\nAccount name must consit of atleast one number. "
                "Please try again"
            )
        return account_name


def existing_customer(account_name):
    """
    Check if account_name is present in google worksheet.
    Store account_name if customer is new.
    if old customer, assess previous balance.
    """

    # Google Spreadsheet
    customers = SHEET.worksheet("customers")

    # get all data in googlesheet and assign them to a variable
    customer_in_database = customers.find(account_name, in_column=1)
    if customer_in_database:

        # Obtain account_name from spreadsheet
        last_transaction = customers.findall(account_name, in_column=1)[-1]

        # Obtain customer balance from last transaction
        balance = customers.row_values(last_transaction.row)[-1]
        code_execution_delay("..................finding customer\n")
        print(f"\nDear {account_name}, Welcome back")
        print(f"You have £{float(balance):.2f}\n")

        return customers, float(balance)
    else:
        code_execution_delay("..................finding customer\n")
        print("You are not a customer yet\n")
        input("Click any key to register with GBPlc: ")
        print(f"\nHi {account_name}, Welcome to GBPlc; the Bank of Champions")
        return account_name, 0


def deposit(user, balance):
    """
    Function to allow customers deposit funds
    """
    deposit_amt = float(input("Enter amount you want to deposit:\n£"))
    current_amt = balance + deposit_amt
    
    # Code to insert customer deposit in google sheet data base
    append_deposit = [user, deposit_amt, "", current_amt]
    SHEET.worksheet("customers").append_row(append_deposit)
    return deposit_amt


def main():
    """
    To perform multiple fuctions
    """
    welcome_to_gracebank()
    user = login()
    check_user, balance = existing_customer(user)

    while True:
        code_execution_delay("---------------")
        print("---Main Menu---")
        print("---------------")
        print("D - Deposit funds")
        print("W - Withdraw funds")
        print("B - Check your balance")
        print("E - Exit bank")

        choice = input("\nEnter your menu choice here: ")
        if choice == "d":
            deposit(check_user, balance)
        elif choice == "w":
            print("withdrawing some money")
        elif choice == "b":
            print("checking my balance")
        elif choice == "e":
            print(f"\nThank you for banking with us, {user}")
        else:
            validate_data(choice)


if __name__ == "__main__":
    main()
