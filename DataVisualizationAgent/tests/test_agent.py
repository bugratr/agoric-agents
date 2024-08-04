
import unittest
from src.DataVisualizationAgent.agent import DataVisualizationAgent

class TestDataVisualizationAgent(unittest.TestCase):
    def setUp(self):
        self.agent = DataVisualizationAgent()

    def test_collect_data(self):
        contract_address = "valid_contract_address"
        result = self.agent.collect_data(contract_address)
        self.assertIsInstance(result, dict)

    def test_analyze_data(self):
        data = {"x": [1, 2, 3], "y": [4, 5, 6]}
        result = self.agent.analyze_data(data)
        self.assertIn("analysis", result)

    def test_visualize_data(self):
        data = {"x": [1, 2, 3], "y": [4, 5, 6]}
        result = self.agent.visualize_data(data)
        self.assertIn("Data visualization saved", result)

if __name__ == "__main__":
    unittest.main()
