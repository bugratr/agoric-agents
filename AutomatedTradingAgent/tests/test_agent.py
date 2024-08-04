
import unittest
from src.AutomatedTradingAgent.agent import AutomatedTradingAgent

class TestAutomatedTradingAgent(unittest.TestCase):
    def setUp(self):
        self.agent = AutomatedTradingAgent()

    def test_collect_market_data(self):
        market = "valid_market"
        result = self.agent.collect_market_data(market)
        self.assertIn("Analyzed market data", result)

    def test_execute_trade(self):
        trade_action = "buy"
        result = self.agent.execute_trade(trade_action)
        self.assertIn("Trade execution successful", result)

if __name__ == "__main__":
    unittest.main()
