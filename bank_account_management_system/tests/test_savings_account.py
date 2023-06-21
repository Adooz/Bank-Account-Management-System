import unittest
from bank_account_management_system.bank_account import BankAccount
from bank_account_management_system.savings_account import SavingsAccount

class SavingsAccountTest(unittest.TestCase):
    def test_interest_calculation(self):
        # Create a SavingsAccount instance
        account = SavingsAccount("123456", "John Doe", 1000.0, 0.05)

        # Calculate interest for one year
        account.calculate_interest()

        # Assert the balance has been updated correctly
        self.assertEqual(account.balance, 1050.0)

if __name__ == '__main__':
    unittest.main()

