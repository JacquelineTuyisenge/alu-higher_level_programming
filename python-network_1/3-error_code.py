#!/usr/bin/python3
# python script that takes in and send request to URL
# then display the body of response ' decode in utf-8'
"""
    send a request to the URL & display body of the response
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
       with urllib.request.urlopen(request) as response:
           print(response.read().decode("ascii"))
    sscept urllib.error.rrrPError as e:
       
