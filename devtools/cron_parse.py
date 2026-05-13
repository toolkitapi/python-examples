"""
DevTools Toolkit — Parse cron expression
==========================================
Parses a cron schedule expression and returns the next N run times
in human-readable form.

Usage: export TOOLKITAPI_KEY=tk_live_...; python cron_parse.py
"""
import json, os, sys
from toolkitapi import Devtools

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

CRON = "0 9 * * 1-5"  # 9 AM Monday–Friday

with Devtools(api_key=API_KEY, base_url="https://dev.toolkitapi.io") as dt:
    result = dt.cron_parse(expression=CRON, count=5, tz="America/New_York")
    print(json.dumps(result, indent=2, default=str))
