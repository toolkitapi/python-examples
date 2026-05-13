"""
DNS Toolkit — SSL certificate inspection
==========================================
Returns TLS certificate details: issuer, validity dates, SANs,
protocol version, cipher suite, and days until expiry.

Usage:
    export TOOLKITAPI_KEY=tk_live_...
    python certificate.py
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
    result = dns.certificate(domain=DOMAIN)
    print(json.dumps(result, indent=2, default=str))
