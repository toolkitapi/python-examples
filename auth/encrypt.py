"""
Auth Toolkit — Encrypt plaintext data (AES-GCM)
=================================================
Usage: export TOOLKITAPI_KEY=tk_live_...; python encrypt.py
"""
import json, os, sys
from toolkitapi import Auth

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Auth(api_key=API_KEY) as auth:
    result = auth.encrypt({
        "plaintext": "Sensitive data: SSN 123-45-6789",
        "key": "0" * 64,  # 32-byte AES-256 key as 64-char hex string
    })
    print(json.dumps(result, indent=2, default=str))
