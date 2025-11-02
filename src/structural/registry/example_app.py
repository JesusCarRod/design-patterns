from structural.registry.registry import Registry
from structural.registry.message_senders import EmailMessageSender, SmsMessageSender, PushMessageSender


def main() -> None:
    def send_message(message_type: str, message: str) -> None:
        message_sender = Registry.get(message_type)
        message_sender.send(message)

    print("::::::::::::::::: Email Message :::::::::::::::::")
    send_message("email", "Hello, how are you?")

    print("::::::::::::::::: SMS Message :::::::::::::::::")
    send_message("sms", "Are you there?")

    print("::::::::::::::::: Push Message :::::::::::::::::")
    send_message("push", "I'm here!")

    print("::::::::::::::::: Invalid Message Type :::::::::::::::::")
    try:
        send_message("invalid", "This is an invalid message type")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
