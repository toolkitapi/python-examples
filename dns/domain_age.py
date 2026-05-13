"""
DNS Toolkit — Domain age
=========================
Returns how old a domain is based on its WHOIS creation date.

Usage:
    export TOOLKITAPI_KEY=tk_live_...
    python domain_age.py
"""

import json
import os
import sys

from toolkitapi import DNS

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY:
    sys.exit("Error: TOOLKITAPI_KEY is not set")

DOMAIN = "github.com"

with DNS(api_key=API_KEY) as dns:
    result = dns.domain_age(domain=DOMAIN)
    print(json.dumps(result, indent=2, default=str))
