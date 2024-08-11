class Wallet:
    def __init__(self, brand):
        self.brand = brand
        self.balance = 0

    def deposit(self, amount):
        assert amount['brand'] == self.brand, "Brand mismatch"
        self.balance += amount['value']
        return self.balance

    def withdraw(self, amount):
        assert amount['brand'] == self.brand, "Brand mismatch"
        if self.balance >= amount['value']:
            self.balance -= amount['value']
            return amount
        else:
            raise ValueError("Insufficient balance")

    def get_balance(self):
        return {'brand': self.brand, 'value': self.balance}

# Usage Example
brand = "Quatloos"
wallet = Wallet(brand)

# Varlık yatırma
amount_to_deposit = {'brand': brand, 'value': 100}
wallet.deposit(amount_to_deposit)
print("Balance after deposit:", wallet.get_balance())

# Varlık çekme
amount_to_withdraw = {'brand': brand, 'value': 50}
withdrawn_amount = wallet.withdraw(amount_to_withdraw)
print("Withdrawn amount:", withdrawn_amount)
print("Balance after withdrawal:", wallet.get_balance())
