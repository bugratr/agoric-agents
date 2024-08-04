
# Usage Guide

## Analyzing Transactions

1. Use the `TransactionAnalyzerAgent` to analyze transactions and generate reports:

   ```python
   from src.TransactionAnalyzerAgent.agent import TransactionAnalyzerAgent

   if __name__ == "__main__":
       agent = TransactionAnalyzerAgent()
       address = "example_address"
       analysis_result = agent.analyze_transactions(address)
       print(analysis_result)
       report_result = agent.generate_report(address)
       print(report_result)
   ```
