
# Usage Guide

## Testing and Validation

1. Use the `TestAndValidationAgent` to test smart contracts, validate applications, and fix errors:

   ```python
   from src.TestAndValidationAgent.agent import TestAndValidationAgent

   if __name__ == "__main__":
       agent = TestAndValidationAgent()
       contract_code = "example_smart_contract_code"
       test_result = agent.test_smart_contract(contract_code)
       print(test_result)
       app_code = "example_application_code"
       validation_result = agent.validate_application(app_code)
       print(validation_result)
       code_with_errors = "example_code_with_errors"
       fixed_code = agent.fix_errors(code_with_errors)
       print(fixed_code)
   ```
