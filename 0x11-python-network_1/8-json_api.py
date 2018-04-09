#!/usr/bin/python3
import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""
    payload = {"q": letter}
    response = requests.post(url, payload)
    try:
        user = response.json()
        if (len(user) < 1):
            print("No result")
        else:
            print("[{}] {}".format(user["id"], user["name"]))
    except:
        print("Not a valid JSON")
