#!/usr/bin/python3
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    headers = response.headers
    print(headers["X-Request-Id"])
