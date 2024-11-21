import os
import shutil
from datetime import datetime

# Paths
project_folder = "D:/pyprojects/TheamsAI"  # Replace with your project folder
backup_folder = "D:/pyprojects/TheamsAI/backup"    # Replace with your backup folder

# Ensure backup folder exists
os.makedirs(backup_folder, exist_ok=True)

# Generate a timestamped folder name
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
destination_folder = os.path.join(backup_folder, f"backup_{timestamp}")

# Exclude the backup folder itself during copying
def exclude_backup_folder(src, names):
    if os.path.abspath(src) == os.path.abspath(backup_folder):
        return names  # Exclude all contents of the backup folder
    return []  # Include everything else

# Perform the backup
try:
    shutil.copytree(project_folder, destination_folder, ignore=exclude_backup_folder)
    print(f"Backup successful! Project backed up to: {destination_folder}")
except Exception as e:
    print(f"Error during backup: {e}")
