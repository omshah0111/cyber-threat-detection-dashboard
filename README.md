# Cyber Threat Detection Dashboard

Python-based cyber threat detection dashboard that parses security logs, flags
suspicious activity (failed logins, potential port scans), and summarizes key
security metrics.

## Features

- Log parsing into structured pandas DataFrames
- Detection of:
  - Repeated failed logins (possible brute force)
  - Multiple distinct ports from a single source IP (possible port scan)
- Simple CLI dashboard summarizing activity and detections

## How to Run

```bash
pip install -r requirements.txt
python src/dashboard.py
