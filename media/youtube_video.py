"""
Media Toolkit — YouTube video metadata
========================================
Returns title, description, duration, view count, thumbnails, and
other metadata for a YouTube video.

Usage: export TOOLKITAPI_KEY=tk_live_...; python youtube_video.py
"""
import json, os, sys
from toolkitapi import Media

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

VIDEO_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

with Media(api_key=API_KEY, base_url="https://youtube.toolkitapi.io") as media:
    result = media.youtube_video(VIDEO_URL)
    print(json.dumps(result, indent=2, default=str))
