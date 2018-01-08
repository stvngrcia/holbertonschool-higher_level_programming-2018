#!/usr/bin/python3
'''
    Unittest for rectangle class
'''
import unittest

Rectangle = __import__('0-rectangle').Rectangle
class TestRectangle(unittest.TestCase):
    '''
        Creating unittest for each intance of the class Rectangle
    '''
    def test_type_class(self):
        '''
            Checks the class of the instance
        '''
        rect = Rectangle()
        self.assertIsInstance(rect, Rectangle)


