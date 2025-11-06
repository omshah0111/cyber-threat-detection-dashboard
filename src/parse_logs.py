import pandas as pd
from dateutil import parser as dt_parser
from pathlib import Path

LOG_COLUMNS = ["timestamp", "source_ip", "dest_ip", "action", "status", "port"]

def parse_log_file(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Log file not found: {path}")

    records = []
    with path.open("r") as f:
        for line in f:
            parts = [p.strip() for p in line.strip().split(",")]
            if len(parts) != len(LOG_COLUMNS):
                continue
            ts, src, dst, action, status, port = parts
            try:
                ts_parsed = dt_parser.isoparse(ts)
                port_int = int(port)
            except Exception:
                continue
            records.append({
                "timestamp": ts_parsed,
                "source_ip": src,
                "dest_ip": dst,
                "action": action,
                "status": status,
                "port": port_int
            })

    df = pd.DataFrame.from_records(records, columns=LOG_COLUMNS)
    df.sort_values("timestamp", inplace=True)
    return df
