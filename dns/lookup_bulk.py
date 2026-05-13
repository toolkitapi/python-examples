"""
DNS Toolkit — Bulk DNS lookup
==============================
Look up DNS records for multiple domains in a single request.

Usage:
    export TOOLKITAPI_KEY=tk_live_...
    python lookup_bulk.py
"""

import json
import os
import sys

from toolkitapi import DNS

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY:
    sys.exit("Error: TOOLKITAPI_KEY is not set")

DOMAINS = ["github.com", "python.org", "nodejs.org"]
RECORD_TYPE = "MX"  # Change to A, TXT, NS, etc.

with DNS(api_key=API_KEY) as dns:
    result = dns.lookup_bulk(DOMAINS, type_=RECORD_TYPE)
    print(json.dumps(result, indent=2, default=str))
