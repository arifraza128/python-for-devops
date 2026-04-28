import shutil
import os
from datetime import datetime
source = "project_folder"
backup_dir = "backups"
if not os.path.exists(backup_dir):
    os.mkdir(backup_dir)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
destination = f"{backup_dir}/backup_{timestamp}"

shutil.copytree(source, destination)

print("Backup created at:", destination)
