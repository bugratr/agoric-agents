
import unittest
from src.APIIntegrationAgent.agent import APIIntegrationAgent

class TestAPIIntegrationAgent(unittest.TestCase):
    def setUp(self):
        self.agent = APIIntegrationAgent()

    def test_call_external_api(self):
        url = "https://api.example.com/data"
        result = self.agent.call_external_api(url)
        self.assertIsInstance(result, dict)

    def test_integrate_with_blockchain(self):
        contract_address = "agoric_contract_address"
        data = {"key": "value"}
        result = self.agent.integrate_with_blockchain(contract_address, data)
        self.assertIn("success", result)

    def test_manage_data_flow(self):
        api_url = "https://api.example.com/data"
        contract_address = "agoric_contract_address"
        result = self.agent.manage_data_flow(api_url, contract_address)
        self.assertIn("success", result)

if __name__ == "__main__":
    unittest.main()
