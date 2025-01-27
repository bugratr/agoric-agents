from autogen import AssistantAgent
from agoric_sdk import Pegasus, Wallet

class AssetManagementAgent:
    def __init__(self):
        self.assistant = AssistantAgent("asset_management_assistant")
        self.pegasus = Pegasus()
        self.wallet = Wallet("ExampleBrand")  # Cüzdanı belirli bir brand ile oluşturun

    def transfer_assets(self, from_address, to_address, amount):
        try:
            # Transfer assets from one address to another using Pegasus
            transfer_result = self.pegasus.transfer(from_address, to_address, amount)
            return transfer_result
        except Exception as e:
            return f"Failed to transfer assets: {str(e)}"

    def get_balance(self, address):
        try:
            # Simulate getting balance by checking the wallet's balance
            balance = self.wallet.get_balance()
            return balance
        except Exception as e:
            return f"Failed to get balance: {str(e)}"

    def generate_asset_report(self, address):
        try:
            # Generate an asset report for the given address
            balance = self.get_balance(address)
            report = self.assistant.handle_input(f"Generate an asset report for the address {address} with balance {balance}")
            return report
        except Exception as e:
            return f"Failed to generate asset report: {str(e)}"

if __name__ == "__main__":
    agent = AssetManagementAgent()
    from_address = "from_example_address"
    to_address = "to_example_address"
    amount = 100
    transfer_result = agent.transfer_assets(from_address, to_address, amount)
    print(transfer_result)
    balance = agent.get_balance(from_address)
    print(balance)
    asset_report = agent.generate_asset_report(from_address)
    print(asset_report)
