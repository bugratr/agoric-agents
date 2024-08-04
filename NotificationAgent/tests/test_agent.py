
import unittest
from src.NotificationAgent.agent import NotificationAgent

class TestNotificationAgent(unittest.TestCase):
    def setUp(self):
        self.agent = NotificationAgent()

    def test_watch_event(self):
        event_name = "valid_event"
        result = self.agent.watch_event(event_name)
        self.assertIsInstance(result, list)

    def test_send_notification(self):
        message = "Test notification"
        result = self.agent.send_notification(message)
        self.assertIn("notification", result)

    def test_generate_report(self):
        events = [{"event": "event1"}, {"event": "event2"}]
        result = self.agent.generate_report(events)
        self.assertIn("report", result)

if __name__ == "__main__":
    unittest.main()
