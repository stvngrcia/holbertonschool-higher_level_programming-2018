#!/usr/bin/python3
import sys
import requests

if __name__ == "__main__":
    user_name = sys.argv[1]
    passwd = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(user_name, passwd))
    try:
        print(response.json()["id"])
    except KeyError:
        print("None")
