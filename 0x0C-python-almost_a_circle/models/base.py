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

    @classmethod
    def create(cls, **dictionary):
        '''
            Returns an instance with all the attributes already set
        '''
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            r2 = Rectangle(3, 8)
        elif cls.__name__ == "Square":
            r2 = Square(5)
        r2.update(**dictionary)
        return (r2)

    @classmethod
    def load_from_file(cls):
        '''
            loading dict representing the parameters for
            and instance and from that creating instances
            then adding those instances to a list that will be
            later returned.

            If the file does not exist it will return an empty
            list.
        '''
        file_name = cls.__name__ + ".json"

        try:
            with open(file_name, encoding="UTF8") as fd:
                content = json.load(fd)
        except:
            return []

        instances = []

        for instance in content:
            tmp = cls.create(**instance)
            instances.append(tmp)

        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''
            Opens a window and draws all the squares and rectangles
        '''
        import turtle

        turtle.penup()
        turtle.goto(-300, 300)

        for instance in list_rectangles:
            turtle.pendown()
            for i in range(2):
                turtle.forward(instance.width)
                turtle.right(90)
                turtle.forward(instance.height)
                turtle.right(90)
            turtle.penup()
            if instance.width < 100:
                move_by = 100
            else:
                move_by = instance.width + 30
            x_cordinate = round(turtle.xcor(), 5)
            turtle.goto(x_cordinate + move_by, 300)

        turtle.goto(-300, 100)
        for instance in list_squares:
            turtle.pendown()
            for i in range(2):
                turtle.forward(instance.width)
                turtle.right(90)
                turtle.forward(instance.height)
                turtle.right(90)
            turtle.penup()
            if instance.width < 100:
                move_by = 100
            else:
                move_by = instance.width + 30
            x_cordinate = round(turtle.xcor(), 5)
            turtle.goto(x_cordinate + move_by, 100)
