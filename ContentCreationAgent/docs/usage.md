
# Usage Guide

## Creating Content

1. Use the `ContentCreationAgent` to create content, write documentation, and prepare educational materials:

   ```python
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
   ```
