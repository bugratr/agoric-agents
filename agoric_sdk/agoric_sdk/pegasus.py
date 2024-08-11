class Pegasus:
    def __init__(self):
        self.transfers = []

    def transfer(self, source, destination, amount):
        transfer_details = {
            'source': source,
            'destination': destination,
            'amount': amount
        }
        self.transfers.append(transfer_details)

    def get_transfers(self):
        return self.transfers
