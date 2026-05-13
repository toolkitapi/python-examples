"""
Barcode Toolkit — Generate a linear barcode (CODE128, EAN-13, etc.)
=====================================================================
Usage: export TOOLKITAPI_KEY=tk_live_...; python generate.py
"""
import json, os, sys
from toolkitapi import Barcode

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Barcode(api_key=API_KEY) as barcode:
    result = barcode.generate({
        "data": "1234567890128",
        "barcode_type": "CODE128",
        "width": 300,
        "height": 100,
    })
    print(json.dumps(result, indent=2, default=str))
