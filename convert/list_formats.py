"""
Convert Toolkit — List all supported formats
=============================================
Returns all supported source and target formats grouped by category
(data, markup, document, spreadsheet, calendar, presentation, ebook).

Usage: export TOOLKITAPI_KEY=tk_live_...; python list_formats.py
"""
import json, os, sys
from toolkitapi import Convert

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Convert(api_key=API_KEY) as convert:
    result = convert.list_all_formats()
    print(json.dumps(result, indent=2, default=str))
