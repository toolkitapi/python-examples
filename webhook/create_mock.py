"""
Webhook Toolkit — Create a mock endpoint
==========================================
Creates a configurable mock HTTP endpoint that returns a predefined
response body, status code, and headers.

Usage: export TOOLKITAPI_KEY=tk_live_...; python create_mock.py
"""
import json, os, sys
from toolkitapi import Webhook

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Webhook(api_key=API_KEY) as webhook:
    result = webhook.create_mock(body={
        "status_code": 200,
        "headers": {"Content-Type": "application/json"},
        "body": '{"ok": true, "message": "Mock response"}',
    })
    print(json.dumps(result, indent=2, default=str))
