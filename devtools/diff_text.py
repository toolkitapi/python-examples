"""
DevTools Toolkit — Text diff
==============================
Returns a unified diff showing the line-by-line changes between
two text strings.

Usage: export TOOLKITAPI_KEY=tk_live_...; python diff_text.py
"""
import json, os, sys
from toolkitapi import Devtools

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Devtools(api_key=API_KEY, base_url="https://dev.toolkitapi.io") as dt:
    result = dt.diff_text({
        "a": "Hello World\nThis is line two\nThis is line three",
        "b": "Hello World\nThis is line 2 (changed)\nThis is line three\nNew fourth line",
    })
    print(json.dumps(result, indent=2, default=str))
