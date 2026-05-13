"""
Scrape Toolkit — Scrape a web page
====================================
Renders a URL with a headless browser and returns HTML, text, or
screenshot output.

Usage: export TOOLKITAPI_KEY=tk_live_...; python scrape.py
"""
import json, os, sys
from toolkitapi import Scrape

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

URL = "https://toolkitapi.io"

with Scrape(api_key=API_KEY) as scrape:
    result = scrape.scrape({"url": URL, "type": "html"})
    print(json.dumps(result, indent=2, default=str))
