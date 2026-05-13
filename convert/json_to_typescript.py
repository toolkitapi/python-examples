"""
Convert Toolkit — JSON to TypeScript interfaces
================================================
Generates TypeScript interfaces from a JSON object or array.

Usage: export TOOLKITAPI_KEY=tk_live_...; python json_to_typescript.py
"""
import json, os, sys
from toolkitapi import Convert

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Convert(api_key=API_KEY) as convert:
    result = convert.json_to_typescript({"data": {"user": {"id": 1, "name": "Alice", "email": "alice@example.com", "active": True, "tags": ["admin", "editor"]}}})
    print(json.dumps(result, indent=2, default=str))
