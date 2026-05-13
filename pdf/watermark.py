"""
PDF Toolkit â€” Add watermark
=============================
Adds a text watermark to every page of a PDF and returns a download
URL for the watermarked version.

Usage: export TOOLKITAPI_KEY=tk_live_...; python watermark.py
"""
import json, os, sys
from toolkitapi import PDF

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with PDF(api_key=API_KEY) as pdf:
    result = pdf.watermark({
        "url": "https://pdfobject.com/pdf/sample.pdf",
        "text": "CONFIDENTIAL",
    })
    print(json.dumps(result, indent=2, default=str))
