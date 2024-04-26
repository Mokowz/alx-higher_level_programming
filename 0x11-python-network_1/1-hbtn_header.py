#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response.

Usage: ./1-hbtn_header.py <URL>
"""
import sys

import urllib.request

url = sys.argv[1]
rqst = urllib.request.Request(url)
with urllib.request.urlopen(rqst) as response:
    print(dict(response.headers).get("X-Request-Id"))
