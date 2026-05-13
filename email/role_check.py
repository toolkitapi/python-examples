"""
Email Toolkit — Role account detection
========================================
Detects whether an email address belongs to a role account
(info@, support@, noreply@, etc.) rather than a real person.

Usage:
    export TOOLKITAPI_KEY=tk_live_...
    python role_check.py
"""
import json, os, sys
from toolkitapi import Email

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

EMAIL = "noreply@github.com"  # Try info@, support@, etc.

with Email(api_key=API_KEY) as email:
    result = email.role_check(email=EMAIL)
    print(json.dumps(result, indent=2, default=str))
