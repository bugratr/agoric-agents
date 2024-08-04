
import unittest
from src.AssetManagementAgent.agent import AssetManagementAgent

class TestAssetManagementAgent(unittest.TestCase):
    def setUp(self):
        self.agent = AssetManagementAgent()

    def test_transfer_assets(self):
        from_address = "valid_from_address"
        to_address = "valid_to_address"
        amount = 100
        result = self.agent.transfer_assets(from_address, to_address, amount)
        self.assertIn("success", result)

    def test_get_balance(self):
        address = "valid_address"
        result = self.agent.get_balance(address)
        self.assertIsInstance(result, int)

    def test_generate_asset_report(self):
        address = "valid_address"
        result = self.agent.generate_asset_report(address)
        self.assertIn("report", result)

if __name__ == "__main__":
    unittest.main()
