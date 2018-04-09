#!/usr/bin/python3

import sys
import requests
import base64


def search_tweets():
    '''
        Script that takes 3 strings
        1.- API key
        2.- API Secret
        3.- String to search
        Displays 5 results.
    '''
    api_key = base64.b64encode(sys.argv[1].encode())
    api_secret = base64.b64encode(sys.argv[2].encode())

    auth = OAuth1(api_key, api_secret)
    url = ' https://api.twitter.com/1.1/search/tweets.json'
    response = requests.get(url, auth=auth)
    print(response.json())

if __name__ == '__main__':
    search_tweets()
