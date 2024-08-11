class Contract:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.instances = []

    def create_instance(self, **initial_args):
        instance = ContractInstance(self, **initial_args)
        self.instances.append(instance)
        return instance

class ContractInstance:
    def __init__(self, contract, **initial_args):
        self.contract = contract
        self.state = initial_args
        self.offers = []
        self.completed = False

    def make_offer(self, offer_args):
        offer = Offer(self, offer_args)
        self.offers.append(offer)
        return offer

    def complete_offer(self, offer):
        # İş mantığı burada uygulanır
        result = f"Offer {offer.args} completed for contract {self.contract.name}"
        offer.completed = True
        self.completed = True
        return result

    def get_payout(self):
        if not self.completed:
            raise ValueError("Contract instance not yet completed")
        return f"Payout for contract {self.contract.name}"

class Offer:
    def __init__(self, contract_instance, args):
        self.contract_instance = contract_instance
        self.args = args
        self.completed = False

# Usage Example
contract_code = "def example_contract_logic(): pass"
contract = Contract("ExampleContract", contract_code)

# Bir sözleşme örneği oluşturun
instance = contract.create_instance(start_value=100)

# Teklif yapın
offer = instance.make_offer({'offer_value': 50})

# Teklifi tamamlayın
result = instance.complete_offer(offer)
print(result)

# Ödeme alın
payout = instance.get_payout()
print(payout)
