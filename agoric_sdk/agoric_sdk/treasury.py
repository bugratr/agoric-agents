class Treasury:
    def __init__(self):
        self.funds = {}

    def add_funds(self, source, amount):
        if source in self.funds:
            self.funds[source] += amount
        else:
            self.funds[source] = amount

    def get_funds(self):
        return self.funds
