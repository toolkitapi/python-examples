"""
Image Toolkit — Resize image
==============================
Resizes an image to the specified width and height and saves the
result to a local file.

Usage: export TOOLKITAPI_KEY=tk_live_...; python resize.py
"""
import json, os, sys
from toolkitapi import Image

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

IMAGE_URL = "https://picsum.photos/seed/toolkitapi/400/300.jpg"
OUTPUT_FILE = "output_resize.jpg"

with Image(api_key=API_KEY) as image:
    result = image.resize(IMAGE_URL, width=200, height=200)
    print(json.dumps(result, indent=2, default=str))
