#!/bin/bash
# Bash script that takes in a URL,sends a GET request to that URL, displays
curl -sI "$1" | grep content-Length | cut -d " " -f 2
