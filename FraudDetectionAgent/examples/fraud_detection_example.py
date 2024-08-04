
from src.FraudDetectionAgent.agent import FraudDetectionAgent

if __name__ == "__main__":
    agent = FraudDetectionAgent()
    address = "example_address"
    fraud_analysis_result = agent.analyze_transactions(address)
    print(fraud_analysis_result)
    alert_result = agent.send_alert("Potential fraud detected!")
    print(alert_result)
    fraud_report_result = agent.generate_fraud_report(address)
    print(fraud_report_result)
