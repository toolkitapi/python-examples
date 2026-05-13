"""
Auth Toolkit — Generate a secure random password
=================================================
Usage: export TOOLKITAPI_KEY=tk_live_...; python generate_password.py
"""
import json, os, sys
from toolkitapi import Auth

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Auth(api_key=API_KEY) as auth:
    result = auth.generate_password(body={
        "length": 20,
        "uppercase": True,
        "lowercase": True,
        "numbers": True,
        "symbols": True,
        "count": 5,  # Generate 5 passwords at once
    })
    print(json.dumps(result, indent=2, default=str))
