"""
Webhook Toolkit — Create a request bin
========================================
Creates a temporary HTTP request bin that captures incoming webhook
requests. Returns a unique bin_id and catch_url.

Usage: export TOOLKITAPI_KEY=tk_live_...; python create_bin.py
"""
import json, os, sys
from toolkitapi import Webhook

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Webhook(api_key=API_KEY) as webhook:
    result = webhook.create_bin()
    print(json.dumps(result, indent=2, default=str))
