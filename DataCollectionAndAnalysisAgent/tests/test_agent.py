
import unittest
from src.DataCollectionAndAnalysisAgent.agent import DataCollectionAndAnalysisAgent

class TestDataCollectionAndAnalysisAgent(unittest.TestCase):
    def setUp(self):
        self.agent = DataCollectionAndAnalysisAgent()

    def test_collect_data(self):
        contract_address = "valid_contract_address"
        result = self.agent.collect_data(contract_address)
        self.assertIn("Analyzed data", result)

if __name__ == "__main__":
    unittest.main()
