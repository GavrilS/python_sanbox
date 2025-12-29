'''
Testing the subtest functionality of unittest.
'''
import unittest

EVEN_NUMBERS = [2, 4, -6, 8, 10, -20, 40, 84]
ODD_NUMBERS = [1, 3, 5, 17, -27, 35, -11, 93]


def is_even(num):
    return num % 2 == 0


class TestIsEven(unittest.TestCase):

    def test_even_number(self):
        for number in EVEN_NUMBERS:
            with self.subTest(number=number):
                self.assertEqual(is_even(number), True)

    def test_odd_number(self):
        for number in ODD_NUMBERS:
            with self.subTest(number=number):
                self.assertEqual(is_even(number), False)


if __name__=='__main__':
    unittest.main(verbosity=2)