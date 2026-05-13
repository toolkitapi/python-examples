"""
PDF Toolkit â€” Extract text
============================
Extracts all readable text from a PDF, preserving page structure.

Usage: export TOOLKITAPI_KEY=tk_live_...; python text_extract.py
"""
import json, os, sys
from toolkitapi import PDF

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with PDF(api_key=API_KEY) as pdf:
    result = pdf.text_extract({
        "url": "https://pdfobject.com/pdf/sample.pdf",
    })
    print(json.dumps(result, indent=2, default=str))
