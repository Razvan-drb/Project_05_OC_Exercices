## Écrivez votre code ici !

class BankAccount:
    def __init__(self, account_holder: str, balance: float):
        self.account_holder = account_holder
        self.balance = balance


    def deposit(self, amount):
        """ method to desposit into the balance, and check if the balance is negative"""
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit amount. Please enter a positive value.")
        return self.balance


    def withdraw(self, amount):
        """ method to withdraw from the balance, and check if the balance is negative if negative dont allow withdraw"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("Invalid withdrawal amount. Please enter a positive value and ensure the balance is sufficient.")
        return self.balance


    def display_balance(self):
        """Method to display the balance and the account holder's name."""
        print(f"Account Holder: {self.account_holder}, Balance: {self.balance}")

account = BankAccount("Alice", 1000.0)
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()















