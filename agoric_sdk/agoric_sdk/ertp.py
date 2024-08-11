class Mint:
    def __init__(self, name):
        self.name = name
        self.total_supply = 0

    def mint(self, amount):
        self.total_supply += amount
        return {
            'brand': self.name,
            'amount': amount
        }

    def get_supply(self):
        return self.total_supply
