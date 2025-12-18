'''
Testing the unittest.TestCase class to help us write our tests.
'''
import unittest

class TestAbsFunciton(unittest.TestCase):

    def test_positive_number(self):
        self.assertEqual(abs(10), 10)

    def test_negative_number(self):
        self.assertEqual(abs(-10), 10)

    def test_zero(self):
        self.assertEqual(abs(0), 0)
