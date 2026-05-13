"""
Geo Toolkit — IP threat intelligence
======================================
Returns threat signals for an IP: VPN, proxy, Tor, datacenter, abuser,
bot, crawler, and overall risk score.

Usage: export TOOLKITAPI_KEY=tk_live_...; python ip_threat.py
"""
import json, os, sys
from toolkitapi import Geo

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

IP = "1.1.1.1"  # Cloudflare DNS

with Geo(api_key=API_KEY) as geo:
    result = geo.ip_threat(IP)
    print(json.dumps(result, indent=2, default=str))
