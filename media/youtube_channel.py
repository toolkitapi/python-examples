"""
Media Toolkit — YouTube channel metadata
==========================================
Returns subscriber count, total views, video count, and channel
details for a given YouTube channel ID.

Usage: export TOOLKITAPI_KEY=tk_live_...; python youtube_channel.py
"""
import json, os, sys
from toolkitapi import Media

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

CHANNEL_ID = "UCVHFbw7woebKtFFbuylTdig"  # ToolkitAPI official channel (placeholder)

with Media(api_key=API_KEY, base_url="https://youtube.toolkitapi.io") as media:
    result = media.youtube_channel(CHANNEL_ID)
    print(json.dumps(result, indent=2, default=str))
