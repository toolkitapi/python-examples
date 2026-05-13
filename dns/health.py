"""
DNS Toolkit — DNS health audit
================================
Audits a domain's DNS configuration and returns a score, grade, and
a list of specific checks (NS redundancy, SPF, DMARC, DNSSEC, etc.).

Usage:
    export TOOLKITAPI_KEY=tk_live_...
    python health.py
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
    result = dns.health(domain=DOMAIN)
    print(json.dumps(result, indent=2, default=str))
