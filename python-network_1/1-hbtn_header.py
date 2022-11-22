#!/usr/bin/python3
# bash script that takes in and send request to URL and display
# the ' X-Request-Id'
"""
    send request to a URL and display the value of 'X-Request-Id'
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
