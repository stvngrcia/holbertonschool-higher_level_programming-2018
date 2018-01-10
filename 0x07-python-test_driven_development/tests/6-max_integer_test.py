#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_none_value(self):
        '''
            Testing when the paratemerter None is passed
        '''
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_right_output(self):
        '''
            Testing when passing and argument that is expected to succeed
        '''
        self.assertEqual(max_integer([1, 6, 100, 4, 0, -1, 10]), 100)

    def test_empty_list(self):
        '''
            Testing an empty list parameter
        '''
        self.assertIsNone(max_integer([]))

    def test_no_param(self):
        '''
            Testing no parameter
        '''
        self.assertIsNone(max_integer())

    def test_equal_values(self):
        '''
            Testing with all the list values equal to each other
        '''
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_no_ints(self):
        '''
            Testing with values in the list that are not integers
        '''
        with self.assertRaises(TypeError):
            max_integer([1, "hello", 2, 3])

    def test_only_negatives(self):
        '''
            Testing with negative numbers
        '''
        self.assertEqual(max_integer([-10, -100, -6, -3, -1]), -1)

    def test_begining(self):
        '''
            Testing with all the list values equal to each other
        '''
        self.assertEqual(max_integer([100, 1, 1, 1]), 100)

    def test_one(self):
        '''
            Testing with all the list values equal to each other
        '''
        self.assertEqual(max_integer([1]), 1)

