from bank_account_management_system.bank_account import BankAccount
from bank_account_management_system.checking_account import CheckingAccount
from bank_account_management_system.savings_account import SavingsAccount

def main():
    # Create a bank account
    account = BankAccount("123456789", "Kingsley Ndonake", 1000.0)

    # Perform actions based on user input
    while True:
        print("\nWelcome to Adooz Bank\n")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            amount = float(input("Enter the deposit amount: "))
            account.deposit(amount)
            print("Deposit successful.")

        elif choice == "2":
            amount = float(input("Enter the withdrawal amount: "))
            if isinstance(account, CheckingAccount):
                account.withdraw_with_fee(amount)
            else:
                account.withdraw(amount)
            print("Withdrawal successful.")

        elif choice == "3":
            print("Account Holder Name: ", account.account_holder_name)
            print("Account Number: ", account.account_number)
            print("Current Balance: ", account.balance)

        elif choice == "4":
            print("Exiting the Bank Account Management System..\n.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

