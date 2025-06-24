# notifier.py

import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_telegram_alert(message: str):
    """
    Sends a message to a specified Telegram chat using the Telegram Bot API.

    This function constructs a request to the Telegram API to send a message
    to a chat identified by the provided chat ID. It uses the bot token for
    authentication. If the message is sent successfully, the function does
    not return any value. If there is an error in sending the message, it
    prints the error message.

    Args:
        message (str): The message to be sent to the Telegram chat.

    Returns:
        None
    """
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    response = requests.post(url, data=data)
    if response.status_code != 200:
        print("Error enviando mensaje:", response.text)
