"""
Convert Toolkit — Convert spreadsheet formats
===============================================
Converts a spreadsheet (XLSX, ODS, CSV) between supported formats
using inline data.

Usage: export TOOLKITAPI_KEY=tk_live_...; python spreadsheet.py
"""
import json, os, sys
from toolkitapi import Convert

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Convert(api_key=API_KEY) as convert:
    result = convert.spreadsheet({
        "data": [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}],
        "from_format": "json",
        "to_format": "xlsx",
    })
    print(json.dumps(result, indent=2, default=str))
