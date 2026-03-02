import os
import shutil

QUARANTINE_FOLDER = "quarantine"

def eliminate_threat(file_path):
    os.makedirs(QUARANTINE_FOLDER, exist_ok=True)

    if not os.path.exists(file_path):
        return "Suspicious file not found"

    destination = os.path.join(QUARANTINE_FOLDER, os.path.basename(file_path))

    if os.path.exists(destination):
        return "File already quarantined"

    shutil.move(file_path, destination)
    return "File moved to quarantine"
