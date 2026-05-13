"""
DevTools Toolkit — Validate JSON
==================================
Checks whether a JSON string is valid and returns parse errors if not.

Usage: export TOOLKITAPI_KEY=tk_live_...; python json_validate.py
"""
import json, os, sys
from toolkitapi import Devtools

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

SAMPLE_JSON = '{"name": "Alice", "age": 30, "active": true}'

with Devtools(api_key=API_KEY, base_url="https://dev.toolkitapi.io") as dt:
    result = dt.json_validate({"data": SAMPLE_JSON})
    print(json.dumps(result, indent=2, default=str))
