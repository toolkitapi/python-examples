"""
Barcode Toolkit — Decode a QR code from a URL
===============================================
Decodes a QR code image and returns the embedded data.

Usage: export TOOLKITAPI_KEY=tk_live_...; python qr_decode.py
"""
import json, os, sys
from toolkitapi import Barcode

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

# Replace with a real QR code image URL
QR_URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Qr-code-ver-10.svg/250px-Qr-code-ver-10.svg.png"

with Barcode(api_key=API_KEY) as barcode:
    result = barcode.qr_decode({"url": QR_URL})
    print(json.dumps(result, indent=2, default=str))
