"""
Barcode Toolkit — Decode a barcode from a URL
===============================================
Decodes any standard barcode (QR, Code128, EAN, etc.) from an image URL.

Usage: export TOOLKITAPI_KEY=tk_live_...; python decode.py
"""
import json, os, sys
from toolkitapi import Barcode

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

BARCODE_URL = "https://upload.wikimedia.org/wikipedia/commons/8/84/EAN13.svg"

with Barcode(api_key=API_KEY) as barcode:
    result = barcode.decode({"url": BARCODE_URL})
    print(json.dumps(result, indent=2, default=str))
