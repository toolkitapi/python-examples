"""
Image Toolkit — Remove background
====================================
Removes the background from an image using AI and saves the
transparent PNG result to a local file.

Usage: export TOOLKITAPI_KEY=tk_live_...; python remove_background.py
"""
import json, os, sys
from toolkitapi import Image

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

IMAGE_URL = "https://picsum.photos/seed/toolkitapi/400/300.jpg"
OUTPUT_FILE = "output_no_bg.png"

with Image(api_key=API_KEY) as image:
    result = image.remove_background(IMAGE_URL)
    print(json.dumps(result, indent=2, default=str))
