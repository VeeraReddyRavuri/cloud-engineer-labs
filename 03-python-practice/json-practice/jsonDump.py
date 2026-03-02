import json

report = {
    "date": "2024-12-12",
    "total-errors": 15,
    "critical": 5,
    "top_errors": ["timeout", "disk full", "Connection refused"]
}

with open("report.json", "w") as f:
    json.dump(report, f, indent=4)