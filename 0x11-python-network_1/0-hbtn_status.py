#!/usr/bin/python3
"""A script that
- fetches https://intranet.hbtn.io/status.
- uses urlib package
"""
from urllib import request

with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    resp = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(resp)))
    print("\t- content: {}".format(resp))
    print("\t- utf8 content: {}".format(resp.decode(encoding='utf-8')))
