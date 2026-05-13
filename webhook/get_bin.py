"""
Webhook Toolkit — Get bin details
===================================
Retrieves metadata for an existing request bin, including its catch
URL, creation time, and request count.

Usage: export TOOLKITAPI_KEY=tk_live_...; python get_bin.py
"""
import json, os, sys
from toolkitapi import Webhook

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

BIN_ID = "your-bin-id-here"  # Replace with a real bin ID from create_bin.py

with Webhook(api_key=API_KEY) as webhook:
    result = webhook.get_bin(BIN_ID)
    print(json.dumps(result, indent=2, default=str))
