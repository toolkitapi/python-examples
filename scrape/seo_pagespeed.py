"""
Scrape Toolkit — PageSpeed / Core Web Vitals
==============================================
Returns Lighthouse performance scores and Core Web Vitals (LCP, FID,
CLS) for a URL.

Usage: export TOOLKITAPI_KEY=tk_live_...; python seo_pagespeed.py
"""
import json, os, sys
from toolkitapi import Scrape

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

URL = "https://toolkitapi.io"

with Scrape(api_key=API_KEY) as scrape:
    result = scrape.seo_pagespeed(URL)
    print(json.dumps(result, indent=2, default=str))
