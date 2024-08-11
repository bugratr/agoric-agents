class Treasury:
    def __init__(self):
        self.funds = {}

    def add_funds(self, source, amount):
        if source in self.funds:
            self.funds[source] += amount
        else:
            self.funds[source] = amount

    def get_funds(self, source):
        return self.funds.get(source, 0)

    def transfer_funds(self, source, destination, amount):
        if self.funds.get(source, 0) >= amount:
            self.funds[source] -= amount
            if destination in self.funds:
                self.funds[destination] += amount
            else:
                self.funds[destination] = amount
        else:
            raise ValueError("Insufficient funds in source")

# Usage Example
treasury = Treasury()

# Fon ekleme
treasury.add_funds("Government", 1000)
print("Funds in Government:", treasury.get_funds("Government"))

# Fon transferi
treasury.transfer_funds("Government", "Education", 200)
print("Funds in Government after transfer:", treasury.get_funds("Government"))
print("Funds in Education after transfer:", treasury.get_funds("Education"))
