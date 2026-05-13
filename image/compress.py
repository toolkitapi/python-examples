"""
Image Toolkit — Compress image
================================
Compresses an image by reducing its quality and saves the result
to a local file.

Usage: export TOOLKITAPI_KEY=tk_live_...; python compress.py
"""
import json, os, sys
from toolkitapi import Image

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

IMAGE_URL = "https://picsum.photos/seed/toolkitapi/400/300.jpg"
OUTPUT_FILE = "output_compress.jpg"

with Image(api_key=API_KEY) as image:
    result = image.compress(IMAGE_URL, quality=75, format="jpeg")
    print(json.dumps(result, indent=2, default=str))
