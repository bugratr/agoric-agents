class ContractInstallation:
    def __init__(self, contract_code):
        self.contract_code = contract_code

class Invitation:
    def __init__(self, contract, offer_args):
        self.contract = contract
        self.offer_args = offer_args

class ZoeService:
    def __init__(self):
        self.installed_contracts = {}
        self.active_offers = []

    def install_contract(self, contract_name, contract_code):
        installation = ContractInstallation(contract_code)
        self.installed_contracts[contract_name] = installation
        return installation

    def make_invitation(self, contract_name, offer_args):
        assert contract_name in self.installed_contracts, "Contract not installed"
        contract = self.installed_contracts[contract_name]
        invitation = Invitation(contract, offer_args)
        return invitation

    def make_offer(self, invitation):
        offer = {'invitation': invitation, 'status': 'pending'}
        self.active_offers.append(offer)
        return offer

    def complete_offer(self, offer):
        offer['status'] = 'completed'
        # Simulate payout process
        payout = "Payout processed based on offer"
        return payout
