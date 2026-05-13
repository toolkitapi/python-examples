"""
Email Toolkit — Security posture check
========================================
Audits a domain's email security configuration: SPF, DMARC, DKIM,
MTA-STS, BIMI, and DNSSEC.

Usage:
    export TOOLKITAPI_KEY=tk_live_...
    python security.py
"""
import json, os, sys
from toolkitapi import Email

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

DOMAIN = "github.com"

with Email(api_key=API_KEY) as email:
    result = email.security(domain=DOMAIN)
    print(json.dumps(result, indent=2, default=str))
