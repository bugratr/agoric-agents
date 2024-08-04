
import requests
from autogen import AssistantAgent
from agoric_sdk import ContractAPI

class APIIntegrationAgent:
    def __init__(self):
        self.assistant = AssistantAgent("api_assistant")
        self.contract_api = ContractAPI("https://api.agoric.net")

    def call_external_api(self, url):
        try:
            # Call the external API
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                return f"API call failed with status code: {response.status_code}"
        except Exception as e:
            return f"Failed to call external API: {str(e)}"

    def integrate_with_blockchain(self, contract_address, data):
        try:
            # Send data to a blockchain contract
            result = self.contract_api.send_data(contract_address, data)
            return result
        except Exception as e:
            return f"Failed to integrate with blockchain: {str(e)}"

    def manage_data_flow(self, api_url, contract_address):
        try:
            # Manage data flow between an external API and a blockchain contract
            api_data = self.call_external_api(api_url)
            if isinstance(api_data, dict):
                integration_result = self.integrate_with_blockchain(contract_address, api_data)
                return integration_result
            else:
                return "Invalid data from API"
        except Exception as e:
            return f"Failed to manage data flow: {str(e)}"

if __name__ == "__main__":
    agent = APIIntegrationAgent()
    api_url = "https://api.example.com/data"
    contract_address = "agoric_contract_address"
    result = agent.manage_data_flow(api_url, contract_address)
    print(result)
