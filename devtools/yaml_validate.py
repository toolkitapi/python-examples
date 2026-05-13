"""
DevTools Toolkit — Validate YAML
==================================
Checks whether a YAML string is syntactically valid.

Usage: export TOOLKITAPI_KEY=tk_live_...; python yaml_validate.py
"""
import json, os, sys
from toolkitapi import Devtools

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

SAMPLE_YAML = "name: Alice\nage: 30\nactive: true\n"

with Devtools(api_key=API_KEY, base_url="https://dev.toolkitapi.io") as dt:
    result = dt.yaml_validate({"data": SAMPLE_YAML})
    print(json.dumps(result, indent=2, default=str))
