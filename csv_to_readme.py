#!/usr/bin/env python3
"""Convert CSV to markdown table and inject into README.md."""

import csv

CSV_FILE = "psgc_links.csv"
README_FILE = "README.md"


def csv_to_markdown(csv_path: str) -> str:
    """Convert CSV file to markdown table."""
    with open(csv_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = next(reader)
        rows = list(reader)
    
    lines = []
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("|" + "|".join("---" for _ in headers) + "|")
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    
    return "\n".join(lines)


def update_readme(readme_path: str, table: str) -> None:
    """Update README.md with the markdown table."""
    with open(readme_path, "r+", encoding="utf-8") as f:
        content = f.read()
        f.seek(0)
        f.write(content.rstrip() + "\n\n## PSGC Updates\n\n" + table + "\n")
        f.truncate()


if __name__ == "__main__":
    table = csv_to_markdown(CSV_FILE)
    update_readme(README_FILE, table)
    print(f"✓ Injected CSV table into {README_FILE}")
