"""
Barcode Toolkit — List supported barcode types
================================================
Returns all supported barcode symbologies.

Usage: export TOOLKITAPI_KEY=tk_live_...; python types.py
"""
import json, os, sys
from toolkitapi import Barcode

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Barcode(api_key=API_KEY) as barcode:
    result = barcode.types()
    print(json.dumps(result, indent=2, default=str))
