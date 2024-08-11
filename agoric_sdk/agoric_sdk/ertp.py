class Brand:
    def __init__(self, name):
        self.name = name

class AmountMath:
    @staticmethod
    def make(brand, value):
        return {'brand': brand, 'value': value}

    @staticmethod
    def add(amount1, amount2):
        assert amount1['brand'] == amount2['brand'], "Brands must match"
        return {'brand': amount1['brand'], 'value': amount1['value'] + amount2['value']}

    @staticmethod
    def subtract(amount1, amount2):
        assert amount1['brand'] == amount2['brand'], "Brands must match"
        assert amount1['value'] >= amount2['value'], "Insufficient amount"
        return {'brand': amount1['brand'], 'value': amount1['value'] - amount2['value']}

class Mint:
    def __init__(self, brand):
        self.brand = brand

    def mint_payment(self, amount):
        assert amount['brand'] == self.brand, "Brands must match"
        return {'payment': amount}

class Issuer:
    def __init__(self, brand):
        self.brand = brand
        self.purses = []

    def make_empty_purse(self):
        purse = {'brand': self.brand, 'amount': {'brand': self.brand, 'value': 0}}
        self.purses.append(purse)
        return purse

    def deposit(self, purse, payment):
        assert purse['brand'] == payment['payment']['brand'], "Brands must match"
        purse['amount'] = AmountMath.add(purse['amount'], payment['payment'])
        return purse

class Purse:
    def __init__(self, issuer):
        self.issuer = issuer
        self.amount = AmountMath.make(issuer.brand, 0)

    def deposit(self, payment):
        self.amount = AmountMath.add(self.amount, payment['payment'])
        return self.amount

    def withdraw(self, amount):
        self.amount = AmountMath.subtract(self.amount, amount)
        return {'payment': amount}
