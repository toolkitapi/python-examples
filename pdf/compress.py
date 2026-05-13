"""
PDF Toolkit â€” Compress PDF
============================
Reduces the file size of a PDF and returns a download URL for the
compressed version.

Usage: export TOOLKITAPI_KEY=tk_live_...; python compress.py
"""
import json, os, sys
from toolkitapi import PDF

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with PDF(api_key=API_KEY) as pdf:
    result = pdf.compress({
        "url": "https://pdfobject.com/pdf/sample.pdf",
    })
    print(json.dumps(result, indent=2, default=str))
