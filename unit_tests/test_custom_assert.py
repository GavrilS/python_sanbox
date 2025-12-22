'''
Testing with custom assert methods.
'''
import unittest

TEST_LIST = [1, 2, 3, 4, 5]


class CustomTestClass(unittest.TestCase):

    def assertListHasItems(self, lis):
        return len(lis) > 0
    

class TestList(CustomTestClass):

    def test_list(self):
        self.assertListHasItems(TEST_LIST)


if __name__=='__main__':
    unittest.main(verbosity=1)