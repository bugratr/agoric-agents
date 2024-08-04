
import unittest
from src.LiquidityProviderAgent.agent import LiquidityProviderAgent

class TestLiquidityProviderAgent(unittest.TestCase):
    def setUp(self):
        self.agent = LiquidityProviderAgent()

    def test_monitor_pools(self):
        result = self.agent.monitor_pools()
        self.assertIsInstance(result, list)

    def test_provide_liquidity(self):
        pool_id = "valid_pool_id"
        amount = 100
        result = self.agent.provide_liquidity(pool_id, amount)
        self.assertIn("success", result)

    def test_withdraw_liquidity(self):
        pool_id = "valid_pool_id"
        amount = 100
        result = self.agent.withdraw_liquidity(pool_id, amount)
        self.assertIn("success", result)

if __name__ == "__main__":
    unittest.main()
