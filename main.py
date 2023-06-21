from bank_account_management_system.bank_account import BankAccount
from bank_account_management_system.savings_account import SavingsAccount
from bank_account_management_system.checking_account import CheckingAccount

# Function to display the main menu
def display_menu():
    print("Adooz Bank - Account Management System")
    print("1. Create a Bank Account")
    print("2. Create a Savings Account")
    print("3. Create a Checking Account")
    print("4. Exit")

# Function to create a bank account
def create_bank_account():
    account_number = input("Enter account number: ")
    account_holder_name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))
    account = BankAccount(account_number, account_holder_name, balance)
    print("Bank Account created successfully!")

# Function to create a savings account
def create_savings_account():
    account_number = input("Enter account number: ")
    account_holder_name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))
    interest_rate = float(input("Enter interest rate: "))
    account = SavingsAccount(account_number, account_holder_name, balance, interest_rate)
    print("Savings Account created successfully!")

# Function to create a checking account
def create_checking_account():
    account_number = input("Enter account number: ")
    account_holder_name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))
    transaction_fee = float(input("Enter transaction fee: "))
    account = CheckingAccount(account_number, account_holder_name, balance, transaction_fee)
    print("Checking Account created successfully!")

# Main program
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            create_bank_account()
        elif choice == '2':
            create_savings_account()
        elif choice == '3':
            create_checking_account()
        elif choice == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

