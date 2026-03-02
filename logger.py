from datetime import datetime

def log_event(message):
    with open("security_logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {message}\n")
