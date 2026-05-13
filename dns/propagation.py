"""
DNS Toolkit — DNS propagation check
=====================================
Checks whether a DNS record has propagated across 20+ global resolvers.
Useful after making DNS changes to see how widely they've spread.

Usage:
    export TOOLKITAPI_KEY=tk_live_...
    python propagation.py
"""

import json
import os
import sys

from toolkitapi import DNS

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY:
    sys.exit("Error: TOOLKITAPI_KEY is not set")

DOMAIN = "github.com"
RECORD_TYPE = "A"  # Change to MX, TXT, NS, etc.

with DNS(api_key=API_KEY) as dns:
    result = dns.propagation(domain=DOMAIN, type_=RECORD_TYPE)
    print(json.dumps(result, indent=2, default=str))
