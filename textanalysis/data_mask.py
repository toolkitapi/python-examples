"""
Text Analysis Toolkit — PII / data masking
============================================
Detects and masks personally identifiable information (phone numbers,
SSNs, email addresses, names, etc.) in a text string.

Usage: export TOOLKITAPI_KEY=tk_live_...; python data_mask.py
"""
import json, os, sys
from toolkitapi import Textanalysis

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

TEXT = "Please call John Smith at 555-867-5309 or email john.smith@example.com about order #SSN-123-45-6789."

with Textanalysis(api_key=API_KEY) as ta:
    result = ta.data_mask({"text": TEXT})
    print(json.dumps(result, indent=2, default=str))
