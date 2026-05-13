"""
Convert Toolkit — Convert markup formats (Markdown ↔ HTML ↔ RST ↔ plain text)
================================================================================
Converts inline markup content between Markdown, HTML, RST, and plain text.

Usage: export TOOLKITAPI_KEY=tk_live_...; python markup.py
"""
import json, os, sys
from toolkitapi import Convert

API_KEY = os.environ.get("TOOLKITAPI_KEY", "")
if not API_KEY: sys.exit("Error: TOOLKITAPI_KEY is not set")

with Convert(api_key=API_KEY) as convert:
    result = convert.markup({
        "content": "# Hello World\n\nThis is a **bold** paragraph with a [link](https://toolkitapi.io).",
        "from_format": "markdown",
        "to_format": "html",
    })
    print(json.dumps(result, indent=2, default=str))
