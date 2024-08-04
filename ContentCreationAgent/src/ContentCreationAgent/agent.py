
from autogen import AssistantAgent

class ContentCreationAgent:
    def __init__(self):
        self.assistant = AssistantAgent("content_assistant")

    def create_content(self, topic):
        try:
            # Generate content for the given topic
            content = self.assistant.handle_input(f"Write an article about {topic}")
            return content
        except Exception as e:
            return f"Failed to create content: {str(e)}"

    def write_documentation(self, topic):
        try:
            # Write documentation for the given topic
            documentation = self.assistant.handle_input(f"Write documentation for {topic}")
            return documentation
        except Exception as e:
            return f"Failed to write documentation: {str(e)}"

    def prepare_educational_materials(self, topic):
        try:
            # Prepare educational materials for the given topic
            materials = self.assistant.handle_input(f"Prepare educational materials for {topic}")
            return materials
        except Exception as e:
            return f"Failed to prepare educational materials: {str(e)}"

if __name__ == "__main__":
    agent = ContentCreationAgent()
    topic = "Agoric blockchain"
    content = agent.create_content(topic)
    print(content)
    documentation = agent.write_documentation(topic)
    print(documentation)
    materials = agent.prepare_educational_materials(topic)
    print(materials)
