#!/usr/bin/python3
import json


def from_json_string(my_str):
    '''
        Converting string into object
    '''
    return (json.loads(my_str))
