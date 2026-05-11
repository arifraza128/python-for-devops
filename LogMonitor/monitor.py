import os
import re
import config
import time
import smtplib
import requests

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from email.mime.text import MIMEText


LOG_FILE = "app.log"

patterns = [
    r"ERROR",
    r"CRITICAL",
    r"500"
]


# slack webhook
SLACK_WEBHOOK = "YOUR_WEBHOOK"


# telegram
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"


# email
EMAIL = "sender@gmail.com"
PASSWORD = "app_password"
TO_EMAIL = "admin@gmail.com"


def send_slack(msg):
    try:
        requests.post(
            SLACK_WEBHOOK,
            json={"text": msg}
        )
        print("slack alert sent")

    except Exception as e:
        print("slack error:", e)


def send_telegram(msg):

    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        data = {
            "chat_id": CHAT_ID,
            "text": msg
        }

        requests.post(url, data=data)

        print("telegram alert sent")

    except Exception as e:
        print("telegram error:", e)


def send_email(msg):

    try:
        message = MIMEText(msg)

        message["Subject"] = "Log Alert"
        message["From"] = EMAIL
        message["To"] = TO_EMAIL

        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()

        server.login(EMAIL, PASSWORD)

        server.sendmail(
            EMAIL,
            TO_EMAIL,
            message.as_string()
        )

        server.quit()

        print("email sent")

    except Exception as e:
        print("mail error:", e)


class LogWatcher(FileSystemEventHandler):

    def __init__(self, file):

        self.file = file
        self.last_position = 0

        if os.path.exists(file):
            self.last_position = os.path.getsize(file)

    def check_logs(self):

        with open(self.file, "r") as f:

            f.seek(self.last_position)

            lines = f.readlines()

            self.last_position = f.tell()

            for line in lines:

                for p in patterns:

                    if re.search(p, line, re.IGNORECASE):

                        alert = f"""
problem found in logs

matched: {p}

log:
{line}
"""

                        print(alert)

                        send_slack(alert)
                        send_telegram(alert)
                        send_email(alert)

    def on_modified(self, event):

        if event.src_path.endswith(self.file):
            self.check_logs()


if __name__ == "__main__":

    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, "w").close()

    event_handler = LogWatcher(LOG_FILE)

    observer = Observer()

    observer.schedule(
        event_handler,
        path=".",
        recursive=False
    )

    observer.start()

    print("watching logs...")

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()

    observer.join()
