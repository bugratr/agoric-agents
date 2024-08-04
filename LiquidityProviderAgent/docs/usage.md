
# Usage Guide

## Providing Liquidity

1. Use the `LiquidityProviderAgent` to monitor pools, provide liquidity, and withdraw liquidity:

   ```python
   from src.LiquidityProviderAgent.agent import LiquidityProviderAgent

   if __name__ == "__main__":
       agent = LiquidityProviderAgent()
       pools = agent.monitor_pools()
       print(pools)
       pool_id = "example_pool_id"
       amount = 100
       add_result = agent.provide_liquidity(pool_id, amount)
       print(add_result)
       remove_result = agent.withdraw_liquidity(pool_id, amount)
       print(remove_result)
   ```
