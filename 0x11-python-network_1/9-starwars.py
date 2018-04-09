#!/usr/bin/python3
import sys
import requests
import json

if __name__ == "__main__":
    search = sys.argv[1]
    url = "https://swapi.co/api/people" + "?search={}".format(search)
    response = requests.get(url)
    json_response = response.json()
    print("Number of results: {}".format(json_response["count"]))
    for name in json_response["results"]:
        print(name["name"])
