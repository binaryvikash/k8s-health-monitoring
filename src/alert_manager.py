import requests
from config import SLACK_WEBHOOK_URL


def send_slack_alert(message):

    if not SLACK_WEBHOOK_URL:
        print("Slack webhook URL not configured.")
        return None

    payload = {
        "text": message
    }

    response = requests.post(
        SLACK_WEBHOOK_URL,
        json=payload
    )

    return response.status_code