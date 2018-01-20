#!/usr/bin/python3
import unittest
from models.square import Square

'''
    Runs test cases for the square module
'''


class test_square(unittest.TestCase):
    '''
        Testing square
    '''

    def setUp(self):
        '''
            Initializing instance with width and height
            parameters
        '''
        self.s = Square(5)

    def tearDown(self):
        '''
            Deleting created instance
        '''
        del self.s

    def test_width(self):
        '''
            Testing the square width getter
        '''
        self.assertEqual(5, self.s.width)

    def test_height(self):
        '''
            Testing the square height getter
        '''
        self.assertEqual(5, self.s.height)

    def test_x(self):
        '''
            Testing square x getter and setter
        '''

        self.s.x = 54
        self.assertEqual(54, self.s.x)
        self.assertEqual(0, self.s.y)

    def test_y(self):
        '''
            Testing square y getter and setter
        '''

        self.s.y = 45
        self.assertEqual(45, self.s.y)
        self.assertEqual(0, self.s.x)

    def test_asquare_id(self):
        '''
            Test the id for square
        '''
        sq = Square(2, 0, 0, 199)
        self.assertEqual(199, sq.id)

    def test_width_string(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square("1")

    def test_width_bool(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(True)

    def test_width_list(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square([10, 6])

    def test_x_string(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(1, "46")

    def test_x_bool(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(1, True)

    def test_x_list(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(1, [10, 6])

    def test_y_string(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(1, 7, "46")

    def test_y_bool(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(1, 7, True)

    def test_y_list(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(1, 7, [10, 6])

    def test_width_negative(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            sq = Square(-4)

    def test_x_negative(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            sq = Square(4, -3)

    def test_y_negative(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            sq = Square(4, 2, -3)

    def test_width_zero(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            sq = Square(0, 5)

    def test_width_float(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(1.07, 5)

    def test_x_float(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(5, 1.07)

    def test_y_float(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(5, 8, 1.07)

    def test_area(self):
        '''
            Testing the area of the square
        '''
        self.assertEqual(self.s.area(), 5 * 5)
        sq = Square(3, 8, 8, 2)
        self.assertEqual(sq.area(), 3 * 3)

    def test_str_overload(self):
        s = Square(5, 8, 7, 88)
        self.assertEqual(s.__str__(), "[Square] (88) 8/7 - 5")

    def test_update_id(self):
        '''
            Testing the update method
        '''
        self.s.update(54)
        self.assertEqual(54, self.s.id)

    def test_update_width(self):
        '''
            Testing the update method
        '''
        self.s.update(54, 30)
        self.assertEqual(30, self.s.width)

    def test_update_height(self):
        '''
            Testing the update method
        '''
        self.s.update(54, 10)
        self.assertEqual(10, self.s.height)

    def test_update_x(self):
        '''
            Testing the update method
        '''
        self.s.update(54, 30, 10)
        self.assertEqual(10, self.s.x)

    def test_update_y(self):
        '''
            Testing the update method
        '''
        self.s.update(54, 30, 6, 2)
        self.assertEqual(2, self.s.y)

    def test_update_dict(self):
        '''
            Testing the update method with **kwargs
        '''
        self.s.update(y=1, size=2, x=3, id=89)
        self.assertEqual(1, self.s.y)
        self.assertEqual(2, self.s.size)
        self.assertEqual(3, self.s.x)
        self.assertEqual(89, self.s.id)

    def test_update_dict_list(self):
        '''
            Testing the update method with **kwargs and *args
        '''
        self.s.update(1000, y=1, width=2, x=3, id=89)
        self.assertEqual(1000, self.s.id)

    def test_update_dict_no_key(self):
        '''
            Testing the update method with **kwargs
        '''
        self.s.update(y=1, size=2, xox=3, id=89)

    def test_update_string(self):
        '''
            Testing the update method with **kwargs
        '''
        self.s.update("str")
        self.assertEqual(self.s.id, "str")


    def test_to_dict(self):
        '''
            Testing the type that is returned from the to_dictionary method
        '''
        r1 = Square(5)
        self.assertEqual(type(r1.to_dictionary()), dict)

    def test_to_dict_print(self):
        '''
            Testing the dict that will be printed
        '''
        r1 = Square(5,0, 0, 410)
        r1_dict = r1.to_dictionary()
        self.assertEqual(r1_dict,
                        {'size': 5, 'id': 410, 'x': 0, 'y': 0})

    def test_missing_height(self):
        '''
            Expecting a type error because height and width are missing
        '''
        with self.assertRaises(TypeError):
            Square()
