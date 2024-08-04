
import unittest
from src.TestAndValidationAgent.agent import TestAndValidationAgent

class TestTestAndValidationAgent(unittest.TestCase):
    def setUp(self):
        self.agent = TestAndValidationAgent()

    def test_test_smart_contract(self):
        contract_code = "valid_smart_contract_code"
        result = self.agent.test_smart_contract(contract_code)
        self.assertIn("test passed", result)

    def test_validate_application(self):
        app_code = "valid_application_code"
        result = self.agent.validate_application(app_code)
        self.assertIn("validated", result)

    def test_fix_errors(self):
        code_with_errors = "code_with_errors"
        result = self.agent.fix_errors(code_with_errors)
        self.assertIn("fixed", result)

if __name__ == "__main__":
    unittest.main()
