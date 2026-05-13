"""
Convert Toolkit — Convert data formats (JSON ↔ CSV ↔ XML ↔ YAML ↔ TOML)
==========================================================================
Converts inline data between JSON, CSV, XML, YAML, and TOML formats.

Usage: export TOOLKITAPI_KEY=tk_live_...; python data.py
"""
import json, os, sys
from toolkitapi import Convert

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Convert(api_key=API_KEY) as convert:
    result = convert.data({
        "data": [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}],
        "from_format": "json",
        "to_format": "csv",
    })
    print(json.dumps(result, indent=2, default=str))
