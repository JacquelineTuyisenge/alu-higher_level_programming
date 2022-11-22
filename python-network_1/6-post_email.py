#!/usr/bin/python3
# python script that takes in a URL and an email address & send POST
# request
"""
    send a POST request to the passed URL with the email as a parameter
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
