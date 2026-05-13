"""
DNS Toolkit — Domain availability check
=========================================
Returns whether a domain name is available to register.

Usage:
    export TOOLKITAPI_KEY=tk_live_...
    python available.py
"""

import json
import os
import sys

from toolkitapi import DNS

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY:
    sys.exit("Error: TOOLKITAPI_KEY is not set")

DOMAIN = "toolkitapi-test-xyz-99999.com"  # Replace with the domain you want to check

with DNS(api_key=API_KEY) as dns:
    result = dns.available(domain=DOMAIN)
    print(json.dumps(result, indent=2, default=str))
