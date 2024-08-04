
import unittest
from src.TransactionAnalyzerAgent.agent import TransactionAnalyzerAgent

class TestTransactionAnalyzerAgent(unittest.TestCase):
    def setUp(self):
        self.agent = TransactionAnalyzerAgent()

    def test_analyze_transactions(self):
        address = "valid_address"
        result = self.agent.analyze_transactions(address)
        self.assertIn("analysis", result)

    def test_generate_report(self):
        address = "valid_address"
        result = self.agent.generate_report(address)
        self.assertIn("report", result)

if __name__ == "__main__":
    unittest.main()
