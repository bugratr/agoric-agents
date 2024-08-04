
# Usage Guide

## Sending Notifications

1. Use the `NotificationAgent` to watch for events, send notifications, and generate reports:

   ```python
   from src.NotificationAgent.agent import NotificationAgent

   if __name__ == "__main__":
       agent = NotificationAgent()
       event_name = "example_event"
       events = agent.watch_event(event_name)
       print(events)
       notification_result = agent.send_notification("Event occurred!")
       print(notification_result)
       report_result = agent.generate_report(events)
       print(report_result)
   ```
