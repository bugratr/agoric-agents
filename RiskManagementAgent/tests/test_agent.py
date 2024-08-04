
import unittest
from src.RiskManagementAgent.agent import RiskManagementAgent

class TestRiskManagementAgent(unittest.TestCase):
    def setUp(self):
        self.agent = RiskManagementAgent()

    def test_monitor_transactions(self):
        result = self.agent.monitor_transactions()
        self.assertIsInstance(result, list)

    def test_notify_user(self):
        message = "Test risk notification"
        response = self.agent.notify_user(message)
        self.assertIn("notification", response)

if __name__ == "__main__":
    unittest.main()
