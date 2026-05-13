"""
Geo Toolkit — Calculate distance between two coordinates
==========================================================
Computes great-circle distance between two lat/lon points in km or miles.

Usage: export TOOLKITAPI_KEY=tk_live_...; python distance.py
"""
import json, os, sys
from toolkitapi import Geo

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Geo(api_key=API_KEY) as geo:
    result = geo.distance({
        "points": [
            {"lat": 51.5074, "lon": -0.1278},  # London
            {"lat": 48.8566, "lon":  2.3522},  # Paris
        ],
        "unit": "km",
    })
    print(json.dumps(result, indent=2, default=str))
