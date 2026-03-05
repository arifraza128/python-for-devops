print('this is my devops working with python')

import psutil

print("CPU Usage:", psutil.cpu_percent(), "%")
print("Memory Usage:", psutil.virtual_memory().percent, "%")
print("Disk Usage:", psutil.disk_usage('/').percent, "%")



from datetime import datetime

now = datetime.now()
print("Current Date & Time:", now)


file = open("test.txt", "w")
file.write("This file is created by Python for DevOps practice.")
file.close()

print("File created successfully")

import requests

def check_server(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f" {url} is UP")
        else:
            print(f" {url} returned status {response.status_code}")
    except requests.exceptions.RequestException:
        print(f"{url} is DOWN")


import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("Command Output:")
        print(result.stdout)
    else:
        print("Error:")
        print(result.stderr)

if __name__ == "__main__":
    run_command("docker ps")

if __name__ == "__main__":
    check_server("https://google.com")


import os

value = os.getenv("PATH")
print("PATH Variable:", value)


name = input("Enter server name: ")
print("Deploying to server:", name)
