from bank_account_management_system.bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance, transaction_fee):
        super().__init_(account_number, account_holder_name, balance)
        self.transaction_fee = transaction_fee

    def withdraw(self, amount):
        super().withdraw(amount)
        self.balance -= self.transaction_fee
