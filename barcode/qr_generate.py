"""
Barcode Toolkit — Generate a QR code
======================================
Returns a QR code image as a URL or base64 string.

Usage: export TOOLKITAPI_KEY=tk_live_...; python qr_generate.py
"""
import json, os, sys
from toolkitapi import Barcode

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Barcode(api_key=API_KEY) as barcode:
    result = barcode.qr_generate({"data": "https://toolkitapi.io", "size": 300})
    print(json.dumps(result, indent=2, default=str))
