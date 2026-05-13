"""
Geo Toolkit — Country information
===================================
Returns details about a country: capital, population, currency, languages,
calling code, and geographic region.

Usage: export TOOLKITAPI_KEY=tk_live_...; python country_info.py
"""
import json, os, sys
from toolkitapi import Geo

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

COUNTRY_CODE = "DE"  # ISO 3166-1 alpha-2

with Geo(api_key=API_KEY) as geo:
    result = geo.country_info(COUNTRY_CODE)
    print(json.dumps(result, indent=2, default=str))
