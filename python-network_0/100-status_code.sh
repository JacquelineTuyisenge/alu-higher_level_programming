#!/bin/bash
# bash script that makes a request to '0.0.0.0:5000/catch_me'
curl -so /dev/null --write-out "%{http_code}" "$1"
