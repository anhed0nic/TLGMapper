"""
aggregate_tlg_json.py

Reads a merged CSV and produces per-provider JSON files.

Output structure:
  <output_dir>/
  ├── provider_index.json
  ├── <ProviderName>/
  │   └── provider.json    (events + variants + field summary)
  └── ...

Usage:
  python aggregate_tlg_json.py

Edit the Configuration section below before running.
"""

import csv
import json
import os
import sys
from collections import defaultdict
from datetime import datetime

# ==========================================================
# Configuration — edit per OS
# ==========================================================

MERGED_CSV = r"C:\output\all_merged.csv"
OUTPUT_DIR = r"C:\output"
OS_LABEL   = "Windows11"

# ==========================================================
# Main
# ==========================================================

def sanitize_dirname(name):
    """Replace characters invalid in directory names."""
    for ch in r'\/:*?"<>|':
        name = name.replace(ch, "_")
    return name


def parse_fields(fields_str):
    """Parse 'Name:Type, Name:Type' into list of strings."""
    if not fields_str or fields_str == "(none)":
        return []
    return [f.strip() for f in fields_str.split(",") if f.strip()]


def build_field_summary(variants):
    """Build a deduplicated field summary across all variants."""
    seen = {}  # "Name:Type" → set of binaries
    for var in variants:
        var_binaries = set(c["binary"] for c in var["callers"])
        for f in var["fields"]:
            if f not in seen:
                seen[f] = set()
            seen[f].update(var_binaries)

    summary = []
    for field_key in sorted(seen.keys()):
        parts = field_key.split(":", 1)
        summary.append({
            "fieldName": parts[0],
            "type": parts[1] if len(parts) > 1 else "Unknown",
            "seenIn": sorted(seen[field_key]),
        })
    return summary


def main():
    if not os.path.exists(MERGED_CSV):
        print(f"[!] Input not found: {MERGED_CSV}")
        sys.exit(1)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    input_mode = "directory" if os.path.isdir(MERGED_CSV) else "file"
    print("=" * 60)
    print(" aggregate_tlg_json — CSV to provider JSON")
    print("=" * 60)
    print(f"  Input  : {MERGED_CSV} ({input_mode})")
    print(f"  Output : {OUTPUT_DIR}")
    print(f"  OS     : {OS_LABEL}")
    print("=" * 60)

    # --- Load CSV(s) ---
    print("[*] Loading CSV...")
    all_rows = []
    has_binary = False

    if os.path.isdir(MERGED_CSV):
        # Directory mode: load each *_tlg.csv, derive Binary from filename
        csv_files = sorted(
            f for f in os.listdir(MERGED_CSV)
            if f.endswith("_tlg.csv")
        )
        if not csv_files:
            print(f"[!] No *_tlg.csv files found in {MERGED_CSV}")
            sys.exit(1)

        print(f"  Found {len(csv_files)} CSV file(s) in directory.")
        for fname in csv_files:
            fpath = os.path.join(MERGED_CSV, fname)
            binary_name = fname.rsplit("_tlg.csv", 1)[0]
            try:
                with open(fpath, "r", encoding="utf-8-sig") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        row["Binary"] = binary_name
                        all_rows.append(row)
            except Exception as e:
                print(f"  [!] Error reading {fname}: {e}")

        has_binary = True

    elif os.path.isfile(MERGED_CSV):
        # Single merged CSV mode
        with open(MERGED_CSV, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            all_rows = list(reader)

        if all_rows:
            cols = list(all_rows[0].keys())
            has_binary = "Binary" in cols
            if not has_binary:
                print("  [!] 'Binary' column not found. Setting to 'Unknown'.")
    else:
        print(f"[!] Input not found: {MERGED_CSV}")
        sys.exit(1)

    if not all_rows:
        print("[!] No data rows loaded.")
        sys.exit(1)

    print(f"  {len(all_rows)} rows loaded.")

    # --- Group by provider ---
    print("[*] Grouping by provider...")
    by_provider = defaultdict(list)
    for row in all_rows:
        # Ensure Binary column exists (derive from filename if missing)
        if not has_binary:
            row["Binary"] = "Unknown"
        prov = row.get("Provider", "Unknown") or "Unknown"
        by_provider[prov].append(row)
    print(f"  {len(by_provider)} provider(s) found.")

    # --- Build per-provider JSON ---
    print("[*] Generating per-provider JSON...")
    index_entries = []

    for prov_name in sorted(by_provider.keys()):
        rows = by_provider[prov_name]

        guid = rows[0].get("GUID", "Unknown")
        binaries = sorted(set(r["Binary"] for r in rows))

        # Group rows by event name
        by_event = defaultdict(list)
        for r in rows:
            by_event[r["Event"]].append(r)

        events_list = []
        total_variants = 0

        for evt_name in sorted(by_event.keys()):
            evt_rows = by_event[evt_name]

            # Group variants by (Level, Keyword, Fields)
            by_variant = defaultdict(list)
            for r in evt_rows:
                var_key = (r["Level"], r["Keyword"], r["Fields"])
                by_variant[var_key].append(r)

            variants = []
            for (level, keyword, fields_str), var_rows in by_variant.items():
                callers = []
                for vr in var_rows:
                    callers.append({
                        "binary": vr["Binary"],
                        "function": vr["Caller"],
                        "ea": vr["InstructionEA"],
                        "confidence": vr["Confidence"],
                    })

                variants.append({
                    "level": int(level) if level.isdigit() else level,
                    "keyword": keyword,
                    "fields": parse_fields(fields_str),
                    "callers": callers,
                })

            field_summary = build_field_summary(variants)
            total_variants += len(variants)

            events_list.append({
                "eventName": evt_name,
                "variantCount": len(variants),
                "variants": variants,
                "fieldSummary": field_summary,
            })

        # --- Write provider.json ---
        prov_obj = {
            "providerName": prov_name,
            "guid": guid,
            "os": OS_LABEL,
            "binaryCount": len(binaries),
            "binaries": binaries,
            "uniqueEventCount": len(events_list),
            "events": events_list,
        }

        safe_name = sanitize_dirname(prov_name)
        prov_dir = os.path.join(OUTPUT_DIR, safe_name)
        os.makedirs(prov_dir, exist_ok=True)

        json_path = os.path.join(prov_dir, "provider.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(prov_obj, f, indent=2, ensure_ascii=False)

        # --- Index entry ---
        index_entries.append({
            "providerName": prov_name,
            "guid": guid,
            "uniqueEventCount": len(events_list),
            "variantCount": total_variants,
            "binaryCount": len(binaries),
            "binaries": binaries,
        })

    # --- Write provider_index.json ---
    index_obj = {
        "os": OS_LABEL,
        "generatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "providerCount": len(index_entries),
        "providers": sorted(index_entries, key=lambda x: x["providerName"]),
    }

    index_path = os.path.join(OUTPUT_DIR, "provider_index.json")
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index_obj, f, indent=2, ensure_ascii=False)

    # --- Summary ---
    total_events = sum(e["uniqueEventCount"] for e in index_entries)
    total_vars = sum(e["variantCount"] for e in index_entries)

    print()
    print("=" * 60)
    print(" Aggregation complete")
    print("=" * 60)
    print(f"  OS              : {OS_LABEL}")
    print(f"  Providers       : {len(index_entries)}")
    print(f"  Unique events   : {total_events}")
    print(f"  Total variants  : {total_vars}")
    print(f"  Index           : {index_path}")
    print(f"  Provider dirs   : {OUTPUT_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()