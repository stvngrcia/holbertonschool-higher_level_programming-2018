#!/usr/bin/python3
'''
    Unittest for rectangle class
'''
import unittest

Rectangle = __import__('2-rectangle').Rectangle
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

        self.assertEqual(r.width, 0)
        self.assertEqual(r.height, 0)

    def test_area(self):
        '''
            test for the area of the rectangle
        '''
        r = Rectangle(2, 5)
        self.assertEqual(r.area(), 10)

    def test_perimeter(self):
        '''
            test for the perimeter of the rectangle
        '''
        r = Rectangle(2, 5)
        self.assertEqual(r.perimeter(), 14)

        r = Rectangle(0, 5)
        self.assertEqual(r.perimeter(), 0)

        r = Rectangle(4, 0)
        self.assertEqual(r.perimeter(), 0)
