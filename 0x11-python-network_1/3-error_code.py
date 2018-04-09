#!/usr/bin/python3

import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError

if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)

    try:
        with urlopen(req) as request:
            data = request.read()
            print(data.decode("utf-8"))
    except HTTPError as error:
        print("Error code: {}".format(error.code))
