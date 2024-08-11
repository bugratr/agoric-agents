class Subscription:
    def __init__(self):
        self.callbacks = []

    def subscribe(self, callback):
        self.callbacks.append(callback)

    def notify_all(self, data):
        for callback in self.callbacks:
            callback(data)

class Notifier:
    def __init__(self):
        self.subscriptions = []

    def create_subscription(self):
        subscription = Subscription()
        self.subscriptions.append(subscription)
        return subscription

    def notify_subscribers(self, data):
        for subscription in self.subscriptions:
            subscription.notify_all(data)

class Updater:
    def __init__(self, notifier):
        self.notifier = notifier
        self.data = None

    def update(self, new_data):
        self.data = new_data
        self.notifier.notify_subscribers(self.data)

# Usage Example
def example_callback(data):
    print(f"Received update: {data}")

notifier = Notifier()

# Create a subscription
subscription = notifier.create_subscription()
subscription.subscribe(example_callback)

# Update data and notify subscribers
updater = Updater(notifier)
updater.update("New Data Available!")
