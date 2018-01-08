#!/usr/bin/python3
'''
    Unittest for rectangle class
'''
import unittest

Rectangle = __import__('1-rectangle').Rectangle
class TestRectangle(unittest.TestCase):
    '''
        Creating unittest for each intance of the class Rectangle
    '''
    def test_type_class(self):
        '''
            Checks the class of the instance
        '''
        r = Rectangle()
        self.assertIsInstance(r, Rectangle)

    def test_typeError(self):
        '''
            Checks for type errors
        '''
        with self.assertRaises(TypeError):
            r = Rectangle("2", 5)

        with self.assertRaises(TypeError):
            r = Rectangle(2, "5")

    def test_valueError(self):
        '''
            Checks for type errors
        '''
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 3)

        with self.assertRaises(ValueError):
            r = Rectangle(1, -3)

    def test_default_val(self):
        '''
            Testing for init default values
        '''
        r = Rectangle()

        self.assertEquals(r.width, 0)
        self.assertEquals(r.height, 0)






