"""
Auth Toolkit — Hash a password (bcrypt / argon2 / scrypt)
============================================================
Usage: export TOOLKITAPI_KEY=tk_live_...; python hash_password.py
"""
import json, os, sys
from toolkitapi import Auth

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Auth(api_key=API_KEY) as auth:
    result = auth.hash_password({"password": "my-secret-password", "algorithm": "bcrypt"})
    print(json.dumps(result, indent=2, default=str))
