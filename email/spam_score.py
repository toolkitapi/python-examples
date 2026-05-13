"""
Email Toolkit — Spam score
===========================
Scores email content against spam filter rules and highlights
which signals trigger a flag.

Usage:
    export TOOLKITAPI_KEY=tk_live_...
    python spam_score.py
"""
import json, os, sys
from toolkitapi import Email

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Email(api_key=API_KEY) as email:
    result = email.spam_score({
        "subject": "URGENT: You won a prize! Click here NOW!!!",
        "body": "Congratulations! You have been selected. Click the link to claim your FREE reward.",
        "from": "noreply@promo-offer.biz",
    })
    print(json.dumps(result, indent=2, default=str))
