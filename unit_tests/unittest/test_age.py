'''
Testing the code that's part of the "age.py" code.
'''
import unittest

from age import get_age_category

class TestGetAgeCategory(unittest.TestCase):
    def test_child(self):
        '''Test for child'''
        self.assertEqual(get_age_category(5), 'Child')

    def test_adolescent(self):
        '''Test for adolescent'''
        self.assertEqual(get_age_category(15), 'Adolescent')

    def test_adult(self):
        '''Test for adult'''
        self.assertEqual(get_age_category(30), 'Adult')

    def test_golden_age(self):
        '''Test for golden aged person'''
        self.assertEqual(get_age_category(80), 'Golden Age')

    def test_age_not_covered(self):
        '''Test for impossible scenario'''
        self.assertEqual(get_age_category(1000), 'Age not covered: 1000')


if __name__=='__main__':
    '''
    Making the test module executable and running the tests with the unittest main function.

    Params:
        verbosity(add docstrings to the test methods for more descriptive output):
            0 -> quiet
            1 -> normal
            2 -> detailed
    '''

    unittest.main(verbosity=2)