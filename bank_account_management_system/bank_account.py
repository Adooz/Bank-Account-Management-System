class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init___(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise InsufficienctFundsError("Insufficent funds. Unable to withdraw.")

    def get_balance(self):
        return self.balance

