"""
Auth Toolkit — Base64 encode data
===================================
Usage: export TOOLKITAPI_KEY=tk_live_...; python base64_encode.py
"""
import json, os, sys
from toolkitapi import Auth

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Auth(api_key=API_KEY) as auth:
    result = auth.base64_encode({"input": "Hello, World! This is a test string."})
    print(json.dumps(result, indent=2, default=str))
