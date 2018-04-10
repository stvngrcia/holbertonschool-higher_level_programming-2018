#!/usr/bin/python3
import sys
import requests


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo_name)
    response = requests.get(url)
    data = response.json()
    count = 0
    for commit in data:
        if count > 9:
            break
        user = commit.get("commit").get("author").get("name")
        print("{}: {}".format(commit.get("sha"), user))

        count += 1
