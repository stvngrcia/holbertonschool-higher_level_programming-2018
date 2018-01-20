#!/usr/bin/python3
import json
'''
    Creating the base class of all other classes for this project.
'''


class Base:
    '''
        This class will manage the id attribute for all the classes.
        Arguments:
            @id: The id for a specific instance.
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        '''
            Converting a dict into a json string
        '''
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
