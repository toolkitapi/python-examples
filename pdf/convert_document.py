"""
PDF Toolkit — Convert document formats
=======================================
Converts a document between formats (e.g. PDF → DOCX) via URL download.

Usage: export TOOLKITAPI_KEY=tk_live_...; python convert_document.py
"""
import json, os, sys
from toolkitapi import PDF

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with PDF(api_key=API_KEY) as pdf:
    result = pdf.convert_document(
        url="https://raw.githubusercontent.com/mozilla/pdf.js/master/examples/learning/helloworld.pdf",
        from_format="pdf",
        to_format="docx",
    )
    if isinstance(result, (bytes, bytearray)):
        print(json.dumps({"status": "ok", "bytes": len(result)}))
    else:
        print(json.dumps(result, indent=2, default=str))
