"""
Scrape Toolkit — Mobile-friendly check
========================================
Tests whether a URL is optimized for mobile devices: viewport meta,
responsive CSS, font sizes, tap target sizes, and more.

Usage: export TOOLKITAPI_KEY=tk_live_...; python seo_mobile_friendly.py
"""
import json, os, sys
from toolkitapi import Scrape

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

URL = "https://toolkitapi.io"

with Scrape(api_key=API_KEY) as scrape:
    result = scrape.seo_mobile_friendly(URL)
    print(json.dumps(result, indent=2, default=str))
