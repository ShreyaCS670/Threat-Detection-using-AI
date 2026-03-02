from detector import detect_threat
from response_engine import eliminate_threat
from logger import log_event

# Simulated suspicious behavior
sample_features = [
    1300,   # file_size
    8.0,    # entropy
    18,     # file changes
    82,     # CPU usage
    73,     # memory usage
    1       # network activity
]

result = detect_threat(sample_features)

if result == 1:
    response = eliminate_threat("fake_malware.exe")
    log_event("Ransomware detected and quarantined")
    print("Threat detected:", response)
else:
    log_event("System safe")
    print("No threat detected")
