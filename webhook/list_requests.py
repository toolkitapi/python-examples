"""
Webhook Toolkit — List captured requests
==========================================
Lists all HTTP requests that have been captured by a request bin.

Usage: export TOOLKITAPI_KEY=tk_live_...; python list_requests.py
"""
import json, os, sys
from toolkitapi import Webhook

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

BIN_ID = "your-bin-id-here"  # Replace with a real bin ID from create_bin.py

with Webhook(api_key=API_KEY) as webhook:
    result = webhook.list_requests(BIN_ID, limit=10)
    print(json.dumps(result, indent=2, default=str))
