#!/bin/bash
# takes in a URL, sends a request to that URL, displays the size of the body
curl -sI "$1" | grep Content-Length | cut -d: -f2 | tr -d " "
