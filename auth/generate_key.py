"""
Auth Toolkit — Generate a cryptographic key / API key / UUID
=============================================================
Generates a random api-key, uuid-v4, nanoid, or secret.

Usage: export TOOLKITAPI_KEY=tk_live_...; python generate_key.py
"""
import json, os, sys
from toolkitapi import Auth

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

KEY_TYPE = "api-key"  # one of: api-key | uuid-v4 | nanoid | secret

with Auth(api_key=API_KEY) as auth:
    result = auth.generate_key(type_=KEY_TYPE)
    print(json.dumps(result, indent=2, default=str))
