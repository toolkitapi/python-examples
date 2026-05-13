"""
Auth Toolkit — Verify a password against a stored hash
========================================================
Usage: export TOOLKITAPI_KEY=tk_live_...; python verify_password.py
"""
import json, os, sys
from toolkitapi import Auth

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Auth(api_key=API_KEY) as auth:
    # Hash a password first, then verify against the result
    hash_resp = auth.hash_password({"password": "my-secret-password"})
    HASH = hash_resp["hash"]
    print("Password hash:", HASH)

    result = auth.verify_password({"password": "my-secret-password", "hash": HASH})
    print(json.dumps(result, indent=2, default=str))
