"""
importing time module that will be used to delay some code execution
"""
from time import sleep
# Import API from Google spreadsheet
import gspread
from google.oauth2.service_account import Credentials
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


def code_execution_delay(information):
    """
    Function to delay execution of some code and allow good
    flow of the program
    """
    print(information)
    sleep(1.5)


def welcome_to_gracebank():
    """
    Welcoming customers to Grace Bank Plc
    """
    gb_logo = pyfiglet.figlet_format("GRACE BANK Plc")
    print(gb_logo)
    print("Hi there! Welcome to Grace Bank Plc. \U0001F3E6\n")
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
            print("Invalid choice, Please try again\n")
    except ValueError:
        print("Invalid choice: Only letters d,w,b,e allowed\n")


def login():
    """
    Customer login their account name which will be verified
    """
    while True:
        account_name = input(
            "\n(For new customers, create an account name "
            "which must have atleast one number) \n"
            "Enter your account name:  "
        ).lower()

        if account_name.isalpha():
            code_execution_delay(
                "\nAccount name must consist of atleast one number. "
                "Please try again\n"
            )
            continue
        elif len(account_name.strip()) == 0:
            print("Account name cannot be empty")
            continue
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
        code_execution_delay("...........finding customer\n")
        print(f"\nDear {account_name}, Welcome back")
        print(f"You have ??{float(balance):.2f}\n")

        return customers, float(balance)
    else:
        code_execution_delay("...........finding customer \u231B\n")
        print("You are not a customer yet\n")
        input("Click any key to register with GBPlc: ")
        print(f"\nHi {account_name}, Welcome to GBPlc; the Bank of Champions")
        return account_name, 0


def deposit(customer, balance):
    """
    Function to allow customers deposit funds. Also allows customers update
    their deposit in google sheet if they add funds to their account
    """
    while True:
        deposit_amt = input("Enter amount you want to deposit:\n??")
        if deposit_amt.replace(".", "", 1).isdigit():
            deposit_amt = float(deposit_amt)

            # Code to insert customer deposit in google sheet data base
            append_deposit = [customer, deposit_amt, "", balance + deposit_amt]
            SHEET.worksheet("customers").append_row(append_deposit)

            code_execution_delay("\n.....transaction ongoing \u231B")
            code_execution_delay("Transaction done! \u2713")
            print(f"??{deposit_amt:.2f} has been deposited to your account\n")
        else:
            print("Invalid entry. Enter valid amount eg 100\n")
            continue
        return deposit_amt


def withdraw(customer, amount):
    """
    Function that allow customer withdraw funds if they have sufficient money.
    Allow overdraft if customer has insufficient funds
    If withdrawal request is greater than account balance, allow customer to
    still withdraw but subtract withdraw request from account balance to
    workout overdraft (i.e amount customer owes the bank)
    """

    while True:
        withdraw_amt = input("Enter amount you want to withdraw:\n??")
        if withdraw_amt.replace(".", "", 1).isdigit():
            withdraw_amt = float(withdraw_amt)
        else:
            print("Invalid entry. Enter valid amount eg 100\n")
            continue

        if withdraw_amt > amount:
            over_draft = withdraw_amt - amount
            code_execution_delay("\nYou have insufficient funds\n")
            print("You've gone into an unarranged overdraft")
            print(f"of ??{over_draft:.2f} but have not been")
            print("charged on this occation.")

        append_withdrawal = [customer, "", withdraw_amt, amount - withdraw_amt]
        SHEET.worksheet("customers").append_row(append_withdrawal)

        code_execution_delay("\n.....transaction ongoing \u231B")
        code_execution_delay("Transaction done! \u2713")
        print(f"??{withdraw_amt:.2f} has been withdrawn to your account\n")
        return withdraw_amt


def check_account_balance(balance):
    """
    Function that allows customer check how much money they have in the bank
    """
    account_balance = balance
    code_execution_delay("...checking account balance \u231B")
    code_execution_delay(f"Your account balance is ??{account_balance:.2f}\n")
    return account_balance


def main():
    """
    To perform multiple fuctions
    """
    welcome_to_gracebank()
    customer = login()
    identify_customer, balance = existing_customer(customer)
    while True:
        code_execution_delay("---------------")
        print("---Main Menu---")
        print("---------------")
        print("D - Deposit funds")
        print("W - Withdraw funds")
        print("B - Check your balance")
        print("E - Exit bank")

        choice = input("\nEnter your menu choice here: ")
        if choice.lower() == "d":
            fund_deposited = deposit(identify_customer, balance)
            balance += fund_deposited
        elif choice.lower() == "w":
            fund_withdrawn = withdraw(customer, balance)
            balance -= fund_withdrawn
        elif choice.lower() == "b":
            check_account_balance(balance)
        elif choice.lower() == "e":
            print(f"\nThank you for banking with us, {customer}")
            quit()
        else:
            validate_data(choice)


if __name__ == "__main__":
    main()
