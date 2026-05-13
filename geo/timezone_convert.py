"""
Geo Toolkit — Timezone conversion
====================================
Converts a datetime string from one timezone to another.

Usage: export TOOLKITAPI_KEY=tk_live_...; python timezone_convert.py
"""
import json, os, sys
from toolkitapi import Geo

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Geo(api_key=API_KEY) as geo:
    result = geo.timezone_convert(
        timestamp="2026-06-15T14:30:00",
        from_="America/New_York",
        to="Asia/Tokyo",
    )
    print(json.dumps(result, indent=2, default=str))
