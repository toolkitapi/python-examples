"""
Email Toolkit — Validate an email address
==========================================
Checks deliverability, MX records, and syntax in one call.

Usage:
    export TOOLKITAPI_KEY=tk_live_...
    python validate_email.py
"""
import json, os, sys
from toolkitapi import Email

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

EMAIL = "user@github.com"  # Replace with the address to validate

with Email(api_key=API_KEY) as email:
    result = email.validate_email(email=EMAIL)
    print(json.dumps(result, indent=2, default=str))
