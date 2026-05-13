"""
Auth Toolkit — Generate a JWT token
=====================================
Usage: export TOOLKITAPI_KEY=tk_live_...; python jwt_generate.py
"""
import json, os, sys
from toolkitapi import Auth

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Auth(api_key=API_KEY) as auth:
    result = auth.jwt_generate({
        "payload": {"sub": "user-123", "role": "admin", "email": "user@example.com"},
        "secret": "my-signing-secret",
        "algorithm": "HS256",
        "expires_in": 3600,
    })
    print(json.dumps(result, indent=2, default=str))
