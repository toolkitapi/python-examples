"""
Scrape Toolkit — Keyword density
==================================
Analyzes the keyword density of a web page and ranks the most
frequently used words and phrases.

Usage: export TOOLKITAPI_KEY=tk_live_...; python seo_keyword_density.py
"""
import json, os, sys
from toolkitapi import Scrape

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

URL = "https://toolkitapi.io"

with Scrape(api_key=API_KEY) as scrape:
    result = scrape.seo_keyword_density(URL)
    print(json.dumps(result, indent=2, default=str))
