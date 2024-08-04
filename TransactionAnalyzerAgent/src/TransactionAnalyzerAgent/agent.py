
from autogen import AssistantAgent
from agoric_sdk import ContractAPI

class TransactionAnalyzerAgent:
    def __init__(self):
        self.assistant = AssistantAgent("analyzer_assistant")
        self.contract_api = ContractAPI("https://api.agoric.net")

    def analyze_transactions(self, address):
        try:
            # Analyze transactions for the given address
            transactions = self.contract_api.get_transactions(address)
            analysis = self.assistant.handle_input(f"Analyze the following transactions: {transactions}")
            return analysis
        except Exception as e:
            return f"Failed to analyze transactions: {str(e)}"

    def generate_report(self, address):
        try:
            # Generate a report for the given address
            transactions = self.contract_api.get_transactions(address)
            report = self.assistant.handle_input(f"Generate a report for the following transactions: {transactions}")
            return report
        except Exception as e:
            return f"Failed to generate report: {str(e)}"

if __name__ == "__main__":
    agent = TransactionAnalyzerAgent()
    address = "example_address"
    analysis_result = agent.analyze_transactions(address)
    print(analysis_result)
    report_result = agent.generate_report(address)
    print(report_result)
