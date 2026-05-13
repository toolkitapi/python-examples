"""
PDF Toolkit â€” Split PDF
=========================
Splits a PDF into a subset of pages and returns a download URL.

Usage: export TOOLKITAPI_KEY=tk_live_...; python split.py
"""
import json, os, sys
from toolkitapi import PDF

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with PDF(api_key=API_KEY) as pdf:
    result = pdf.split({
        "url": "https://pdfobject.com/pdf/sample.pdf",
        "pages": "1",
    })
    print(json.dumps(result, indent=2, default=str))
