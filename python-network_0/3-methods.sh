#!/bin/bash
# bash script takes in URL and displays all HTTP methods the server accept
curl -sI "$1" | grep "Allow:" | cut -d "" -f2-#!/bin/bash
# bash script takes in URL and displays all HTTP methods the server accept
curl -sI "$1" | grep "Allow:" | cut -d "" -f2-
