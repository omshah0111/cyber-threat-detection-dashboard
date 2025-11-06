from pathlib import Path
from parse_logs import parse_log_file
from detect_threats import detect_brute_force, detect_port_scans, summarize_activity

def main():
    log_path = Path(__file__).parent.parent / "data" / "sample_logs.log"
    df = parse_log_file(log_path)
    summary = summarize_activity(df)
    print("=== Overview ===")
    print(summary)

    print("\n=== Brute Force Attempts ===")
    brute = detect_brute_force(df)
    print(brute if not brute.empty else "None detected.")

    print("\n=== Port Scans ===")
    scans = detect_port_scans(df)
    print(scans if not scans.empty else "None detected.")

if __name__ == "__main__":
    main()
