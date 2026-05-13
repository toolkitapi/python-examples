"""
Auth Toolkit — Generate a TOTP secret and QR code
===================================================
Returns a TOTP secret + a QR code URL you can scan with any
authenticator app (Google Authenticator, Authy, etc.).

Usage: export TOOLKITAPI_KEY=tk_live_...; python totp_generate.py
"""
import json, os, sys
from toolkitapi import Auth

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Auth(api_key=API_KEY) as auth:
    result = auth.totp_generate(
        issuer="MyApp",
        account_name="user@example.com",
        digits=6,
        period=30,
    )
    print(json.dumps(result, indent=2, default=str))
