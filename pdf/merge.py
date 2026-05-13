"""
PDF Toolkit — Merge PDFs
==========================
Merges two or more PDF files into a single PDF and returns a
download URL for the result.

Usage: export TOOLKITAPI_KEY=tk_live_...; python merge.py
"""
import json, os, sys
from toolkitapi import PDF

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with PDF(api_key=API_KEY) as pdf:
    result = pdf.merge({
        "pdf_urls": [
            "https://pdfobject.com/pdf/sample.pdf",
            "https://pdfobject.com/pdf/sample.pdf",
        ]
    })
    print(json.dumps(result, indent=2, default=str))
