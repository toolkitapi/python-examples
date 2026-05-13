"""
Email Toolkit — Identify email provider
=========================================
Returns the email provider name, type, and MX record details
for a given domain or email address.

Usage:
    export TOOLKITAPI_KEY=tk_live_...
    python provider.py
"""
import json, os, sys
from toolkitapi import Email

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

DOMAIN = "github.com"  # Can also pass a full email address

with Email(api_key=API_KEY) as email:
    result = email.provider(domain=DOMAIN)
    print(json.dumps(result, indent=2, default=str))
