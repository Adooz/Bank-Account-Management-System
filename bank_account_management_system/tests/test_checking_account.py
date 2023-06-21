import unittest
from bank_account_management_system.bank_account import BankAccount
from bank_account_management_system.checking_account import CheckingAccount

class CheckingAccountTest(unittest.TestCase):
    def test_withdraw_transaction_fee(self):
        # Create a CheckingAccount instance
        account = CheckingAccount("123456", "John Doe", 1000.0, 5.0)

        # Withdraw an amount
        account.withdraw(100.0)

        # Assert the balance has been updated correctly
        self.assertEqual(account.balance, 895.0)

if __name__ == '__main__':
    unittest.main()

