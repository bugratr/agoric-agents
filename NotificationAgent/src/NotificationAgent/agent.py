
from autogen import AssistantAgent
from agoric_sdk import ContractAPI

class NotificationAgent:
    def __init__(self):
        self.assistant = AssistantAgent("notification_assistant")
        self.contract_api = ContractAPI("https://api.agoric.net")

    def watch_event(self, event_name):
        try:
            # Watch for a specific event
            events = self.contract_api.get_events(event_name)
            return events
        except Exception as e:
            return f"Failed to watch event: {str(e)}"

    def send_notification(self, message):
        try:
            # Send a notification
            notification = self.assistant.handle_input(message)
            return notification
        except Exception as e:
            return f"Failed to send notification: {str(e)}"

    def generate_report(self, events):
        try:
            # Generate a report based on the events
            report = self.assistant.handle_input(f"Generate a report for the following events: {events}")
            return report
        except Exception as e:
            return f"Failed to generate report: {str(e)}"

if __name__ == "__main__":
    agent = NotificationAgent()
    event_name = "example_event"
    events = agent.watch_event(event_name)
    print(events)
    notification_result = agent.send_notification("Event occurred!")
    print(notification_result)
    report_result = agent.generate_report(events)
    print(report_result)
