
from src.DataCollectionAndAnalysisAgent.agent import DataCollectionAndAnalysisAgent

if __name__ == "__main__":
    agent = DataCollectionAndAnalysisAgent()
    contract_address = "your_contract_address_here"
    result = agent.collect_data(contract_address)
    print(result)
