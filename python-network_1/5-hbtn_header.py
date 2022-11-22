#!/usr/bin/python3
# python script that takes in and sende request to URL & display value
# of varilable 'X-Request-Id' in the response header
"""
    display values of variable 'X-Request-Id' in the response header
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
