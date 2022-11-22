#!/usr/bin/python3
# python script that fetches 'https://alu-intranet.hbtn.io/status'
"""
    fetch 'https://intranet.hbtn.io/status'
"""
import requests


if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
