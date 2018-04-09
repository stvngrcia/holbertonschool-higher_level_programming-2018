#!/usr/bin/python3
import sys
import requests


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(repo_name, owner)
    response = requests.get(url)
    json_response = response.json()
    counter = 0
    for commit in json_response:
        if counter > 9:
            break
        user = commit["commit"]["author"]["name"]
        print("{}: {}".format(commit["sha"], user))
        counter += 1
