"""File writers. Boilerplate: gzipped CSV with header, gzipped JSON Lines."""

import csv
import gzip
import json
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path
from typing import Any


def _default(value: Any) -> Any:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, Decimal):
        return str(value)
    raise TypeError(f"Not JSON serializable: {type(value).__name__}")


def write_csv_gz(rows: list[dict[str, Any]], path: Path) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows to write for {path.name}")
    fieldnames = list(rows[0].keys())
    with gzip.open(path, "wt", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="raise")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: _default(v) if isinstance(v, (date, datetime, Decimal)) else v
                             for k, v in row.items()})
    return len(rows)


def write_jsonl_gz(rows: list[dict[str, Any]], path: Path) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, default=_default, separators=(",", ":")))
            f.write("\n")
    return len(rows)
