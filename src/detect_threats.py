import pandas as pd

def detect_brute_force(df: pd.DataFrame, fail_threshold: int = 5) -> pd.DataFrame:
    failed = df[(df["action"] == "LOGIN") & (df["status"] == "FAIL")]
    counts = failed.groupby("source_ip").size().reset_index(name="failed_login_count")
    return counts[counts["failed_login_count"] >= fail_threshold]

def detect_port_scans(df: pd.DataFrame, port_threshold: int = 4) -> pd.DataFrame:
    grouped = df.groupby("source_ip")["port"].nunique().reset_index(name="unique_ports"]
    )
    return grouped[grouped["unique_ports"] >= port_threshold]

def summarize_activity(df: pd.DataFrame) -> dict:
    return {
        "total_logs": len(df),
        "unique_source_ips": df["source_ip"].nunique(),
        "actions": df["action"].value_counts().to_dict(),
        "statuses": df["status"].value_counts().to_dict(),
    }
