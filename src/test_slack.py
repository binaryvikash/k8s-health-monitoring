from alert_manager import send_slack_alert

status = send_slack_alert(
    "🚨 Test Alert from Kubernetes Health Monitor"
)

print(f"HTTP Status Code: {status}")