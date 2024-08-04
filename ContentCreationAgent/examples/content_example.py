
from src.ContentCreationAgent.agent import ContentCreationAgent

if __name__ == "__main__":
    agent = ContentCreationAgent()
    topic = "Agoric blockchain"
    content = agent.create_content(topic)
    print(content)
    documentation = agent.write_documentation(topic)
    print(documentation)
    materials = agent.prepare_educational_materials(topic)
    print(materials)
