
from src.AutomatedTradingAgent.agent import AutomatedTradingAgent

if __name__ == "__main__":
    agent = AutomatedTradingAgent()
    market = "agoric_market"
    trade_action = "buy"
    market_data = agent.collect_market_data(market)
    print(market_data)
    trade_result = agent.execute_trade(trade_action)
    print(trade_result)
