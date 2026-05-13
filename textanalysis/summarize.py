"""
Text Analysis Toolkit — Summarize text
========================================
Extracts key sentences to produce a concise summary of longer text.

Usage: export TOOLKITAPI_KEY=tk_live_...; python summarize.py
"""
import json, os, sys
from toolkitapi import Textanalysis

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

TEXT = (
    "Artificial intelligence (AI) is intelligence demonstrated by machines, "
    "as opposed to the natural intelligence displayed by animals including humans. "
    "AI research has been defined as the field of study of intelligent agents, "
    "which refers to any system that perceives its environment and takes actions "
    "that maximize its chance of achieving its goals. The term 'artificial "
    "intelligence' had previously been used to describe machines that mimic and "
    "display human cognitive skills associated with the human mind, such as learning "
    "and problem-solving."
)

with Textanalysis(api_key=API_KEY) as ta:
    result = ta.summarize({"text": TEXT, "max_sentences": 2})
    print(json.dumps(result, indent=2, default=str))
