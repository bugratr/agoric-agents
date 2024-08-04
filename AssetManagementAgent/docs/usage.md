
# Usage Guide

## Managing Assets

1. Use the `AssetManagementAgent` to transfer assets, check balances, and generate reports:

   ```python
   from src.AssetManagementAgent.agent import AssetManagementAgent

   if __name__ == "__main__":
       agent = AssetManagementAgent()
       from_address = "from_example_address"
       to_address = "to_example_address"
       amount = 100
       transfer_result = agent.transfer_assets(from_address, to_address, amount)
       print(transfer_result)
       balance = agent.get_balance(from_address)
       print(balance)
       asset_report = agent.generate_asset_report(from_address)
       print(asset_report)
   ```
