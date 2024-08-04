
import unittest
from src.GovernanceVotingAgent.agent import GovernanceVotingAgent

class TestGovernanceVotingAgent(unittest.TestCase):
    def setUp(self):
        self.agent = GovernanceVotingAgent()

    def test_start_voting(self):
        proposal = "Test Proposal"
        result = self.agent.start_voting(proposal)
        self.assertIn("started", result)

    def test_collect_votes(self):
        voting_id = "valid_voting_id"
        result = self.agent.collect_votes(voting_id)
        self.assertIsInstance(result, dict)

    def test_announce_results(self):
        voting_id = "valid_voting_id"
        result = self.agent.announce_results(voting_id)
        self.assertIn("Voting ID", result)

if __name__ == "__main__":
    unittest.main()
