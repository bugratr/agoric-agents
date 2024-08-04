
from src.APIIntegrationAgent.agent import APIIntegrationAgent

if __name__ == "__main__":
    agent = APIIntegrationAgent()
    api_url = "https://api.example.com/data"
    contract_address = "agoric_contract_address"
    result = agent.manage_data_flow(api_url, contract_address)
    print(result)
