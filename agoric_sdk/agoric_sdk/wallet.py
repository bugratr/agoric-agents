class Wallet:
    def __init__(self):
        self.balance = {}

    def deposit(self, currency, amount):
        if currency in self.balance:
            self.balance[currency] += amount
        else:
            self.balance[currency] = amount

    def withdraw(self, currency, amount):
        if currency in self balance and self.balance[currency] >= amount:
            self.balance[currency] -= amount
        else:
            raise ValueError("Insufficient funds")

    def get_balance(self):
        return self.balance
