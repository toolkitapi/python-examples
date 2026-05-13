"""
DNS Toolkit — Lookup all record types at once
===============================================
Queries A, AAAA, MX, TXT, CNAME, NS, SOA, CAA, and SRV records in a
single request and returns everything found.

Usage:
    export TOOLKITAPI_KEY=tk_live_...
    python lookup_all.py
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
    result = dns.lookup_all(domain=DOMAIN)
    print(json.dumps(result, indent=2, default=str))
