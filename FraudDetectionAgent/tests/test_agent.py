
import unittest
from src.FraudDetectionAgent.agent import FraudDetectionAgent

class TestFraudDetectionAgent(unittest.TestCase):
    def setUp(self):
        self.agent = FraudDetectionAgent()

    def test_analyze_transactions(self):
        address = "valid_address"
        result = self.agent.analyze_transactions(address)
        self.assertIn("analysis", result)

    def test_send_alert(self):
        message = "Test alert"
        result = self.agent.send_alert(message)
        self.assertIn("alert", result)

    def test_generate_fraud_report(self):
        address = "valid_address"
        result = self.agent.generate_fraud_report(address)
        self.assertIn("report", result)

if __name__ == "__main__":
    unittest.main()
