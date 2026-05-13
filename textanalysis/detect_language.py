"""
Text Analysis Toolkit — Detect language
=========================================
Identifies the language of a text string with a confidence score.

Usage: export TOOLKITAPI_KEY=tk_live_...; python detect_language.py
"""
import json, os, sys
from toolkitapi import Textanalysis

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

TEXT = "Bonjour, comment allez-vous aujourd'hui?"

with Textanalysis(api_key=API_KEY) as ta:
    result = ta.detect_language({"text": TEXT})
    print(json.dumps(result, indent=2, default=str))
