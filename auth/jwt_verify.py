"""
Auth Toolkit — Verify and decode a JWT token
==============================================
Usage: export TOOLKITAPI_KEY=tk_live_...; python jwt_verify.py
"""
import json, os, sys
from toolkitapi import Auth

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

# Generate a token and immediately verify it
SECRET = "my-signing-secret"

with Auth(api_key=API_KEY) as auth:
    token_resp = auth.jwt_generate({
        "payload": {"sub": "user-123", "role": "admin"},
        "secret": SECRET,
        "algorithm": "HS256",
        "expires_in": 3600,
    })
    TOKEN = token_resp["token"]
    print("Generated token:", TOKEN[:40], "...")

    result = auth.jwt_verify({"token": TOKEN, "secret": SECRET})
    print(json.dumps(result, indent=2, default=str))
