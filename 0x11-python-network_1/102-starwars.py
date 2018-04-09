#!/usr/bin/python3
import sys
import requests


def print_people(url, flag):
    '''
        Handling pagination and printing all the people
    '''
    if url is None:
        return
    response = requests.get(url)
    json_response = response.json()
    if flag == 1:
        print("Number of results: {}".format(json_response["count"]))
    for name in json_response["results"]:
        print(name["name"])
        print_films(name["films"])
    url = json_response["next"]
    print_people(url, 0)


def print_films(films):
    '''
        prints all the fims in a list
    '''
    for film in films:
        response = requests.get(film)
        film_name = response.json()["title"]
        print("\t{}".format(film_name))

if __name__ == "__main__":
    search = sys.argv[1]
    people = []
    url = "https://swapi.co/api/people" + "?search={}".format(search)
    print_people(url, 1)
