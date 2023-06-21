class BankAccount:
    def __init__(self, account_number, account_holder_name, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} to {self.account_holder_name}.")
        else:
            print("Invalid amount. Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount} from account {self.account_number}.")
            else:
                print("Insufficient funds. Unable to withdraw.")
        else:
            print("Invalid amount. Withdrawal amount must be greater than 0.")

    def check_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")
        return self.balance

