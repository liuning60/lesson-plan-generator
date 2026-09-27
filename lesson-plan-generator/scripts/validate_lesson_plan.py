#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson-plan data validator (lesson-plan-generator v1.1)
=======================================================
Automatically checks the hard constraints of a generated lesson plan:
  1) phase minutes in the time arrangement sum == session total (e.g. 4 hours = 180 min)
  2) image count >= the minimum for the course type (lab/practice 6, mixed 5, theory 4;
     override with --min-images)

Input: a text file or stdin, one entry per line:
  total_minutes=180      # session total in minutes (required)
  min_images=6           # image minimum (optional, default 4)
  images=6               # actual image count for this session (optional, default 0)
  Introduction=10        # phase=minutes (any number of phases, Chinese names fine)
  Lecture=40
  Demo=15
  Student independent practice=45
  Teacher roving coaching=15
  Summary & comments=25
  # lines starting with # are comments; blank lines ignored

Usage:
  python validate_lesson_plan.py plan_data.txt
  python validate_lesson_plan.py --min-images 5 < plan_data.txt

Exit codes: 0 = pass; 1 = constraints not met; 2 = input error / unparseable
Output: JSON report (phases, sums, verdict)
"""
import argparse
import json
import re
import sys

def parse_line(line):
    """Parse a 'name=value' line; value must be an integer. Returns (key, value) or None."""
    line = line.strip()
    if not line or line.startswith("#"):
        return None
    if "=" not in line:
        return None
    key, _, val = line.partition("=")
    key = key.strip()
    val = val.strip()
    if not re.fullmatch(r"\d+", val):
        return None
    return key, int(val)

def main():
    ap = argparse.ArgumentParser(description="Lesson-plan hard-constraint check: time budget + image minimums")
    ap.add_argument("file", nargs="?", help="data file path; default reads stdin")
    ap.add_argument("--min-images", type=int, default=None,
                    help="image minimum, overrides min_images in data (default 4)")
    args = ap.parse_args()

    try:
        if args.file:
            with open(args.file, "r", encoding="utf-8") as f:
                raw = f.read()
        else:
            raw = sys.stdin.read()
    except OSError as e:
        print(json.dumps({"success": False, "error": f"read failed: {e}"}, ensure_ascii=False))
        return 2

    total_minutes = None
    min_images = None
    images = 0
    phases = []
    parse_errors = []

    for lineno, line in enumerate(raw.splitlines(), 1):
        parsed = parse_line(line)
        if parsed is None:
            if line.strip() and not line.lstrip().startswith("#") and "=" in line:
                parse_errors.append({"line": lineno, "text": line.strip()})
            continue
        key, val = parsed
        if key == "total_minutes":
            total_minutes = val
        elif key == "min_images":
            min_images = val
        elif key == "images":
            images = val
        else:
            phases.append((key, val))

    if args.min_images is not None:
        min_images = args.min_images

    problems = []
    if total_minutes is None:
        problems.append("missing total_minutes (session total)")
    else:
        phase_sum = sum(v for _, v in phases)
        if phase_sum != total_minutes:
            problems.append(f"phase minutes sum {phase_sum} != session total {total_minutes}")
        if not phases:
            problems.append("no teaching phases parsed")

    if min_images is None:
        min_images = 4
    if images < min_images:
        problems.append(f"image count {images} < minimum {min_images}")

    report = {
        "success": len(problems) == 0 and total_minutes is not None,
        "total_minutes": total_minutes,
        "phase_sum": sum(v for _, v in phases) if phases else 0,
        "phases": phases,
        "min_images": min_images,
        "images": images,
        "problems": problems,
        "parse_errors": parse_errors,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if parse_errors:
        return 2
    return 0 if len(problems) == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
