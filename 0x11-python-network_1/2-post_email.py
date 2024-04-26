#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.

Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import urllib.request
import urllib.parse

url = sys.argv[1]
email = {"email": sys.argv[2]}
data = urllib.parse.urlencode(email).encode("ascii")

req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    print(response.read().decode("utf-8"))