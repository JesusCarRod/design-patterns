from structural.registry.message_sender import MessageSender
from structural.registry.registry import Registry


@Registry.register("email")
class EmailMessageSender(MessageSender):
    def send(self, message: str) -> None:
        print(f"Sending email: {message}")


@Registry.register("sms")
class SmsMessageSender(MessageSender):
    def send(self, message: str) -> None:
        print(f"Sending SMS: {message}")


@Registry.register("push")
class PushMessageSender(MessageSender):
    def send(self, message: str) -> None:
        print(f"Sending push notification: {message}")
