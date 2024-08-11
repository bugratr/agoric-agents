class Zoe:
    def __init__(self):
        self.contracts = []

    def add_contract(self, contract):
        self.contracts.append(contract)

    def get_contracts(self):
        return self.contracts
