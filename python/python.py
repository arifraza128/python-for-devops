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