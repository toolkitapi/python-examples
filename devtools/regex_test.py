"""
DevTools Toolkit — Regex test
================================
Tests a regular expression pattern against an input string and
returns all matches.

Usage: export TOOLKITAPI_KEY=tk_live_...; python regex_test.py
"""
import json, os, sys
from toolkitapi import Devtools

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Devtools(api_key=API_KEY, base_url="https://dev.toolkitapi.io") as dt:
    result = dt.regex_test({
        "pattern": r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",
        "text": "Server at 192.168.1.1 and backup at 10.0.0.254 are online.",
    })
    print(json.dumps(result, indent=2, default=str))
