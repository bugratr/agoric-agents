
from src.RiskManagementAgent.agent import RiskManagementAgent

if __name__ == "__main__":
    agent = RiskManagementAgent()
    risk_analysis = agent.monitor_transactions()
    for risk in risk_analysis:
        notification = agent.notify_user(risk)
        print(notification)
