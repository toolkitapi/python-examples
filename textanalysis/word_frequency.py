"""
Text Analysis Toolkit — Word frequency
========================================
Returns the most common words and their frequencies in a text block.

Usage: export TOOLKITAPI_KEY=tk_live_...; python word_frequency.py
"""
import json, os, sys
from toolkitapi import Textanalysis

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

TEXT = (
    "The quick brown fox jumps over the lazy dog. "
    "The dog barked at the fox. The fox ran away quickly. "
    "It was a quick escape for the brown fox."
)

with Textanalysis(api_key=API_KEY) as ta:
    result = ta.word_frequency({"text": TEXT, "top_n": 10})
    print(json.dumps(result, indent=2, default=str))
