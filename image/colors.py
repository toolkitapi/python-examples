"""
Image Toolkit — Extract dominant colors
=========================================
Analyzes an image and returns the dominant color palette with hex
codes and percentage coverage.

Usage: export TOOLKITAPI_KEY=tk_live_...; python colors.py
"""
import json, os, sys
from toolkitapi import Image

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

IMAGE_URL = "https://picsum.photos/seed/toolkitapi/400/300.jpg"

with Image(api_key=API_KEY) as image:
    result = image.colors({"url": IMAGE_URL})
    print(json.dumps(result, indent=2, default=str))
