import requests
from config import SLACK_WEBHOOK_URL


def send_slack_alert(message):

    payload = {
        "text": message
    }

    response = requests.post(
        SLACK_WEBHOOK_URL,
        json=payload
    )

    return response.status_code