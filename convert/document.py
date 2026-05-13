"""
Convert Toolkit — Convert document formats
===========================================
Converts a document (Word, HTML, PDF, etc.) between supported formats
using a publicly accessible URL.

Usage: export TOOLKITAPI_KEY=tk_live_...; python document.py
"""
import json, os, sys
from toolkitapi import Convert

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Convert(api_key=API_KEY) as convert:
    result = convert.document({
        "url": "https://filesamples.com/samples/document/docx/sample1.docx",
        "from_format": "docx",
        "to_format": "pdf",
    })
    print(json.dumps(result, indent=2, default=str))
