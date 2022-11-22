#!/usr/bin/python3
# python script that takes in URL & email then send POST request
# response body of response
"""
    takes in URL & email then sendes POST request
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
