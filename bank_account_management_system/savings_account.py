from bank_account_management_system.bank_account import BankAccount



class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance, interest_rate):
        super().__init__(account_number, account_holder_name, balance)
        self.interest_rate = interest_rate
    
    def deposit(self, amount):
        super().deposit(amount) #calls the parent class's deposit method
        interest = self.balance * self.interest_rate
        self.balance += interest

