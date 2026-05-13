"""
Email Toolkit — Batch email validation
========================================
Validate multiple email addresses in a single request.

Usage:
    export TOOLKITAPI_KEY=tk_live_...
    python validate_batch.py
"""
import json, os, sys
from toolkitapi import Email

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Email(api_key=API_KEY) as email:
    result = email.validate_batch({
        "emails": ["user@github.com", "invalid@notareal.xyz", "noreply@python.org"]
    })
    print(json.dumps(result, indent=2, default=str))
