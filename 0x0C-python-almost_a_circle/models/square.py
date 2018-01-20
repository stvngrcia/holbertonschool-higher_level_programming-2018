#!/usr/bin/python3
'''
    Implementation of the square class
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
        Inherits from:
            Rectanle
            Base
    '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''
            Overwritting the ste method
        '''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                    self.width)
