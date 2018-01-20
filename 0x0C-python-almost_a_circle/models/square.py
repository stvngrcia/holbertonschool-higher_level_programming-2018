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

    def __str__(self):
        '''
            Overwritting the ste method
        '''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                    self.width)
