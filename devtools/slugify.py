"""
DevTools Toolkit — Slugify a string
=====================================
Converts a human-readable string into a URL-safe slug.

Usage: export TOOLKITAPI_KEY=tk_live_...; python slugify.py
"""
import json, os, sys
from toolkitapi import Devtools

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

TEXT = "Hello World! This is a Test String — with punctuation."

with Devtools(api_key=API_KEY, base_url="https://dev.toolkitapi.io") as dt:
    result = dt.slugify({"text": TEXT})
    print(json.dumps(result, indent=2, default=str))
