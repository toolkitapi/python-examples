"""
Geo Toolkit — Phone number validation and parsing
==================================================
Validates an international phone number and returns carrier, line type,
country, and formatted versions.

Usage: export TOOLKITAPI_KEY=tk_live_...; python phone_validate.py
"""
import json, os, sys
from toolkitapi import Geo

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

PHONE = "+14155552671"  # E.164 format

with Geo(api_key=API_KEY) as geo:
    result = geo.phone_validate(PHONE)
    print(json.dumps(result, indent=2, default=str))
