
import unittest
from src.ComplianceCheckAgent.agent import ComplianceCheckAgent

class TestComplianceCheckAgent(unittest.TestCase):
    def setUp(self):
        self.agent = ComplianceCheckAgent()

    def test_check_compliance(self):
        transaction = "valid_transaction"
        result = self.agent.check_compliance(transaction)
        self.assertIn("compliant", result)

    def test_report_non_compliance(self):
        transaction = "non_compliant_transaction"
        result = self.agent.report_non_compliance(transaction)
        self.assertIn("report", result)

    def test_generate_compliance_report(self):
        transactions = ["transaction1", "transaction2"]
        result = self.agent.generate_compliance_report(transactions)
        self.assertIn("report", result)

if __name__ == "__main__":
    unittest.main()
