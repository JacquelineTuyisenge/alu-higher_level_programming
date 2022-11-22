#!/usr/bin/python3
# bash script that fetches 'https://alu-intranet.hbtn.io/status'
""" fetch 'https://alu-intranet.hbtn.io/status' """
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request("https://alu-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print(" - type: {}".format(type(body)))
        print(" - content: {}".format(body))
        print(" - utf8 content: {}".format(body.decode(utf8-8")))
