"""
Geo Toolkit — IP geolocation lookup
=====================================
Returns city, country, lat/lon, timezone, and ASN for an IP address.

Usage: export TOOLKITAPI_KEY=tk_live_...; python ip_lookup.py
"""
import json, os, sys
from toolkitapi import Geo

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

IP = "8.8.8.8"  # Google Public DNS

with Geo(api_key=API_KEY) as geo:
    result = geo.ip_lookup(IP)
    print(json.dumps(result, indent=2, default=str))
