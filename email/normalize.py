"""
Email Toolkit — Normalize an email address
============================================
Normalizes Gmail dot-tricks, plus-aliases, and provider-specific
quirks so you can deduplicate addresses reliably.

Usage:
    export TOOLKITAPI_KEY=tk_live_...
    python normalize.py
"""
import json, os, sys
from toolkitapi import Email

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

EMAIL = "user.name+tag@gmail.com"  # Try dot/plus Gmail variants

with Email(api_key=API_KEY) as email:
    result = email.normalize(email=EMAIL)
    print(json.dumps(result, indent=2, default=str))
