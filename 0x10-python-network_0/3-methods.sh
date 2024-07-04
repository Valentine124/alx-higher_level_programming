#!/bin/bash
# List the HTTP methods using curl
curl -s -X OPTIONS -I $1 | grep "Allow:" | awk -F': ' '{print $2}'
