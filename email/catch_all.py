"""
Email Toolkit — Catch-all detection
=====================================
Returns whether a domain accepts all email addresses regardless of
whether the mailbox exists (catch-all / accept-all configuration).

Usage:
    export TOOLKITAPI_KEY=tk_live_...
    python catch_all.py
"""
import json, os, sys
from toolkitapi import Email

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

DOMAIN = "github.com"  # Replace with the domain to check

with Email(api_key=API_KEY) as email:
    result = email.catch_all(domain=DOMAIN)
    print(json.dumps(result, indent=2, default=str))
