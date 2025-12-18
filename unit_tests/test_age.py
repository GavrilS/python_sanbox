'''
Testing the code that's part of the "age.py" code.
'''
import unittest

from age import get_age_category

class TestGetAgeCategory(unittest.TestCase):
    def test_child(self):
        self.assertEqual(get_age_category(5), 'Child')

    def test_adolescent(self):
        self.assertEqual(get_age_category(15), 'Adolescent')

    def test_adult(self):
        self.assertEqual(get_age_category(30), 'Adult')

    def test_golden_age(self):
        self.assertEqual(get_age_category(80), 'Golden Age')

    def test_age_not_covered(self):
        self.assertEqual(get_age_category(1000), 'Age not covered: 1000')


if __name__=='__main__':
    '''
    Making the test module executable and running the tests with the unittest main function.

    Params:
        verbosity:
            0 -> quiet
            1 -> normal
            2 -> detailed
    '''

    unittest.main(verbosity=1)