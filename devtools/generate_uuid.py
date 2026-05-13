"""
DevTools Toolkit — Generate UUID(s)
=====================================
Generates one or more UUIDs. Supports v4 (random) and v1 (time-based).

Usage: export TOOLKITAPI_KEY=tk_live_...; python generate_uuid.py
"""
import json, os, sys
from toolkitapi import Devtools

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Devtools(api_key=API_KEY, base_url="https://dev.toolkitapi.io") as dt:
    result = dt.generate_uuid(version="v4", count=5)
    print(json.dumps(result, indent=2, default=str))
