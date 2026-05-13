"""
DNS Toolkit — Typosquat detection
====================================
Returns a list of lookalike domains generated using common typosquatting
techniques (insertion, deletion, replacement, homoglyphs, etc.), plus
whether each variant resolves to a live IP address.

Usage:
    export TOOLKITAPI_KEY=tk_live_...
    python typosquat.py
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
    result = dns.typosquat(domain=DOMAIN)
    print(json.dumps(result, indent=2, default=str))
