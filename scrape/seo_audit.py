"""
Scrape Toolkit — SEO audit
============================
Runs a comprehensive SEO audit on a URL: title, meta tags, headings,
canonical, structured data, and more.

Usage: export TOOLKITAPI_KEY=tk_live_...; python seo_audit.py
"""
import json, os, sys
from toolkitapi import Scrape

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

URL = "https://toolkitapi.io"

with Scrape(api_key=API_KEY) as scrape:
    result = scrape.seo_audit(URL)
    print(json.dumps(result, indent=2, default=str))
