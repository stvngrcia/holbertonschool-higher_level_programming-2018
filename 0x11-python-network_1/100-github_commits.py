#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    import requests

    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    res = requests.get(url)
    commits = res.json()
    count = 0
    for commit in commits:
        sha = commit.get("sha")
        name = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, name))
        count += 1
        if count == 10:
            break
