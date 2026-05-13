"""
Webhook Toolkit — Hit a mock endpoint
=======================================
Sends a POST request to a mock endpoint and receives the configured
response. Useful for testing client code that calls webhooks.

Usage: export TOOLKITAPI_KEY=tk_live_...; python hit_mock.py
"""
import json, os, sys
from toolkitapi import Webhook

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

MOCK_ID = "your-mock-id-here"  # Replace with a real mock ID from create_mock.py

with Webhook(api_key=API_KEY) as webhook:
    result = webhook.hit_mock(MOCK_ID)
    print(json.dumps(result, indent=2, default=str))
