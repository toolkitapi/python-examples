"""
Text Analysis Toolkit — Text similarity
=========================================
Computes cosine similarity between two text strings (0.0 – 1.0).

Usage: export TOOLKITAPI_KEY=tk_live_...; python text_similarity.py
"""
import json, os, sys
from toolkitapi import Textanalysis

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Textanalysis(api_key=API_KEY) as ta:
    result = ta.text_similarity({
        "a": "The quick brown fox jumps over the lazy dog",
        "b": "A fast brown fox leaps across a sleepy dog",
    })
    print(json.dumps(result, indent=2, default=str))
