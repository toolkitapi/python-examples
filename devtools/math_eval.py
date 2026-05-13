"""
DevTools Toolkit — Math expression evaluator
==============================================
Safely evaluates a mathematical expression and returns the result.

Usage: export TOOLKITAPI_KEY=tk_live_...; python math_eval.py
"""
import json, os, sys
from toolkitapi import Devtools

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

EXPRESSION = "sqrt(144) + (2^10 / 4)"  # Change this to test different expressions

with Devtools(api_key=API_KEY, base_url="https://dev.toolkitapi.io") as dt:
    result = dt.math_eval({"expression": EXPRESSION})
    print(json.dumps(result, indent=2, default=str))
