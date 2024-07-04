#!/bin/bash
# Send a request to a URL using cURL

curl -s $1 | wc -c