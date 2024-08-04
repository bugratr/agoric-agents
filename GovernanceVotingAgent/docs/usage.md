
# Usage Guide

## Governance Voting

1. Use the `GovernanceVotingAgent` to start voting, collect votes, and announce results:

   ```python
   from src.GovernanceVotingAgent.agent import GovernanceVotingAgent

   if __name__ == "__main__":
       agent = GovernanceVotingAgent()
       proposal = "Should we implement feature X?"
       start_result = agent.start_voting(proposal)
       print(start_result)
       voting_id = "example_voting_id"
       results = agent.announce_results(voting_id)
       print(results)
   ```
