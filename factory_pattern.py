
from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self, text: str) -> None:
        pass

class EmailNotification(Notification):
    def send(self, text: str) -> None:
        print(f"[Email] Sending message to inbox: '{text}'")


class SMSNotification(Notification):
    def send(self, text: str) -> None:
        print(f"[SMS] Sending text message to phone: '{text}'")


class PushNotification(Notification):
    def send(self, text: str) -> None:
        print(f"[Push Notification] Displaying mobile banner: '{text}'")

class NotificationFactory:
    @staticmethod
    def get_notifier(channel_type: str) -> Notification:
        channels = {
            "email": EmailNotification,
            "sms": SMSNotification,
            "push": PushNotification
        }
        chosen_class = channels.get(channel_type.lower())
        if not chosen_class:
            raise ValueError(f"Unknown channel: {channel_type}")
        return chosen_class()

if __name__ == "__main__":
    test_channels = ["email", "sms", "push"]

    for channel in test_channels:
        notifier = NotificationFactory.get_notifier(channel)
        notifier.send("Your delivery is on its way!")