#!/usr/bin/python3
'''
    Implementation of the square class
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
        Inherits from:
            Rectangle
            Base
    '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''
            returning the width of the square though its getter
        '''
        return self.width

    @size.setter
    def size(self, val):
        '''
            setting the width and height throught their setters
        '''
        self.setter_validation("width", val)
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        '''
            Updates the arguments in the class
        '''

        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        '''
            Returns a dictionary representation of this class
        '''
        return {'id': getattr(self, "id"),
                'x': getattr(self, "x"),
                'size': getattr(self, "size"),
                'y': getattr(self, "y")}

    def __str__(self):
        '''
            Overwritting the ste method
        '''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
