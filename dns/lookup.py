"""
DNS Toolkit — Lookup DNS records
=================================
Look up A, AAAA, MX, TXT, CNAME, NS, SOA, CAA, or SRV records for a domain.

Usage:
    export TOOLKITAPI_KEY=tk_live_...
    python lookup.py
"""

import json
import os
import sys

from toolkitapi import DNS

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY:
    sys.exit("Error: TOOLKITAPI_KEY is not set")

DOMAIN = "github.com"
RECORD_TYPE = "A"  # Change to MX, TXT, AAAA, NS, etc.

with DNS(api_key=API_KEY) as dns:
    result = dns.lookup(domain=DOMAIN, type_=RECORD_TYPE)
    print(json.dumps(result, indent=2, default=str))
