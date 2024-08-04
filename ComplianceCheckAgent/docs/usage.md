
# Usage Guide

## Checking Compliance

1. Use the `ComplianceCheckAgent` to check transactions for compliance, report non-compliance, and generate compliance reports:

   ```python
   from src.ComplianceCheckAgent.agent import ComplianceCheckAgent

   if __name__ == "__main__":
       agent = ComplianceCheckAgent()
       transaction = "example_transaction"
       compliance_result = agent.check_compliance(transaction)
       print(compliance_result)
       report_result = agent.report_non_compliance(transaction)
       print(report_result)
       transactions = ["transaction1", "transaction2"]
       compliance_report = agent.generate_compliance_report(transactions)
       print(compliance_report)
   ```
