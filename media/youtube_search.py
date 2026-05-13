"""
Media Toolkit — YouTube search
================================
Searches YouTube for videos matching a query and returns a ranked
list of results with metadata.

Usage: export TOOLKITAPI_KEY=tk_live_...; python youtube_search.py
"""
import json, os, sys
from toolkitapi import Media

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

QUERY = "python REST API tutorial"

with Media(api_key=API_KEY, base_url="https://youtube.toolkitapi.io") as media:
    result = media.youtube_search(QUERY)
    print(json.dumps(result, indent=2, default=str))
