
import unittest
from src.ContentCreationAgent.agent import ContentCreationAgent

class TestContentCreationAgent(unittest.TestCase):
    def setUp(self):
        self.agent = ContentCreationAgent()

    def test_create_content(self):
        topic = "Blockchain"
        content = self.agent.create_content(topic)
        self.assertIn("Blockchain", content)

    def test_write_documentation(self):
        topic = "Smart Contracts"
        documentation = self.agent.write_documentation(topic)
        self.assertIn("Smart Contracts", documentation)

    def test_prepare_educational_materials(self):
        topic = "Decentralized Finance"
        materials = self.agent.prepare_educational_materials(topic)
        self.assertIn("Decentralized Finance", materials)

if __name__ == "__main__":
    unittest.main()
