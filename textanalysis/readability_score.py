"""
Text Analysis Toolkit — Readability score
===========================================
Computes Flesch-Kincaid, Gunning Fog, SMOG, and other readability
indexes for a block of text.

Usage: export TOOLKITAPI_KEY=tk_live_...; python readability_score.py
"""
import json, os, sys
from toolkitapi import Textanalysis

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

TEXT = (
    "The cat sat on the mat. It was a sunny day. "
    "The children played outside in the park near the old oak tree."
)

with Textanalysis(api_key=API_KEY) as ta:
    result = ta.readability_score({"text": TEXT})
    print(json.dumps(result, indent=2, default=str))
