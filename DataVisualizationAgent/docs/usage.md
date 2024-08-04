
# Usage Guide

## Visualizing Data

1. Use the `DataVisualizationAgent` to collect, analyze, and visualize data:

   ```python
   from src.DataVisualizationAgent.agent import DataVisualizationAgent

   if __name__ == "__main__":
       agent = DataVisualizationAgent()
       contract_address = "example_contract_address"
       data = agent.collect_data(contract_address)
       print(data)
       analysis_result = agent.analyze_data(data)
       print(analysis_result)
       visualization_result = agent.visualize_data(data)
       print(visualization_result)
   ```
