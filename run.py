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
            if menu_choice != d or menu_choice != w:
                print("Invalid choice, Try again")
            if menu_choice != d or menu_choice != e:
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

    customer_in_database = customers.find(account_name, in_column=1)
    print(customers)
    print(customer_in_database)
    data = customers.get_all_values()
    print(data)


user = login()


existing_customer(user)
    # if customer_in_database:

    #     # Find username from database (spreadsheet)
    #     last_cell = customers.findall(account_name, in_column=1)[-1]
    #     # Gets user previus balance from the spreadsheet
    #     balance = customers.row_values(last_cell.row)[-1]
    #     code_execution_delay("User checking....\n")
    #     code_execution_delay("User found")
    #     code_execution_delay(
    #         f"\nWelcome back {account_name}.. "
    #         f"Your current account balance is: £{float(balance):.2f}\n"
    #     )

    #     return account_name, float(balance)
    # else:
    #     code_execution_delay("User checking....")
    #     print("\nUsername not found\n" "Creating new user...")
    #     time.sleep(1.4)
    #     print(f"\nHello {account_name}, Thanx for joining GBPlc")
    #     return account_name, 0


def main():
    """
    To perform multiple fuctions
    """
    welcome_to_gracebank()
    user = login()
    # check_user, balance = existing_customer(user)

    while True:
        code_execution_delay("------------------")
        print("GBPlc Main Menu")
        print("D - Deposit funds")
        print("W - Withdraw funds")
        print("B - Check your balance")
        print("E - Exit bank")


# if __name__ == "__main__":
#     main()
