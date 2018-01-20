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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
            Converting a dict into a json string
        '''
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
            Writes the string representation of an object of a class
            into a file
        '''
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, encoding="UTF8") as fd:
                content = json.load(fd)
        except:
            content = []
        if list_objs is not None:
            for item in list_objs:
                item = item.to_dictionary()
                json_dict = json.loads(cls.to_json_string(item))
                content.append(json_dict)

        with open(file_name, mode="w") as fd:
            json.dump(content, fd)
