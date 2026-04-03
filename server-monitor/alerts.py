import smtplib
from email.mime.text import MIMEText
import requests
import config

# Send Email Alert
def send_email(subject, message):
    try:
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = config.EMAIL_SENDER
        msg['To'] = config.EMAIL_RECEIVER

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(config.EMAIL_SENDER, config.EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        print(" Email alert sent")
    except Exception as e:
        print(" Email error:", e)


# Send Slack Alert
def send_slack(message):
    try:
        payload = {"text": message}
        response = requests.post(config.SLACK_WEBHOOK_URL, json=payload)

        if response.status_code == 200:
            print(" Slack alert sent")
        else:
            print(" Slack error:", response.text)
    except Exception as e:
        print(" Slack exception:", e)
