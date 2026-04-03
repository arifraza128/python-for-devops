import psutil
import time
import config
from alerts import send_email, send_slack

def check_system():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    print(f"CPU: {cpu}%, RAM: {ram}%, DISK: {disk}%")

    alerts = []

    if cpu > config.CPU_THRESHOLD:
        alerts.append(f" High CPU Usage: {cpu}%")

    if ram > config.RAM_THRESHOLD:
        alerts.append(f" High RAM Usage: {ram}%")

    if disk > config.DISK_THRESHOLD:
        alerts.append(f" High Disk Usage: {disk}%")

    if alerts:
        message = "\n".join(alerts)

        # Send Alerts
        send_email(" Server Alert", message)
        send_slack(message)

def main():
    while True:
        check_system()
        time.sleep(10)   

if __name__ == "__main__":
    main()
