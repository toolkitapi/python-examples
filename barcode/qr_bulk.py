"""
Barcode Toolkit — Bulk QR code generation
===========================================
Generate multiple QR codes in a single request.

Usage: export TOOLKITAPI_KEY=tk_live_...; python qr_bulk.py
"""
import json, os, sys
from toolkitapi import Barcode

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Barcode(api_key=API_KEY) as barcode:
    result = barcode.qr_bulk({
        "items": [
            {"data": "https://toolkitapi.io", "size": 200},
            {"data": "https://github.com", "size": 200},
            {"data": "Contact: Jane Doe | jane@example.com", "size": 300},
        ]
    })
    print(json.dumps(result, indent=2, default=str))
