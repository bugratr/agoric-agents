class Pegasus:
    def __init__(self):
        self.transfers = []

    def transfer(self, source, destination, amount):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        transfer_details = {
            'source': source,
            'destination': destination,
            'amount': amount
        }
        self.transfers.append(transfer_details)
        return transfer_details

    def get_transfers(self):
        return self.transfers

    def verify_transfer(self, transfer_details):
        if transfer_details in self.transfers:
            return True
        else:
            return False

# Usage Example
pegasus = Pegasus()

# Token transferi
transfer = pegasus.transfer("BlockchainA", "BlockchainB", 100)
print("Transfer completed:", transfer)

# Yapılan transferlerin listesi
all_transfers = pegasus.get_transfers()
print("All transfers:", all_transfers)

# Bir transferin doğrulanması
is_valid = pegasus.verify_transfer(transfer)
print("Is the transfer valid?", is_valid)
