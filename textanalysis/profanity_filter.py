"""
Text Analysis Toolkit — Profanity filter
==========================================
Detects and optionally masks profanity / offensive words in text.

Usage: export TOOLKITAPI_KEY=tk_live_...; python profanity_filter.py
"""
import json, os, sys
from toolkitapi import Textanalysis

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

TEXT = "This is a clean sentence with no bad words in it at all."

with Textanalysis(api_key=API_KEY) as ta:
    result = ta.profanity_filter({"text": TEXT})
    print(json.dumps(result, indent=2, default=str))
