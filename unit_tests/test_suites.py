import unittest

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def check_substring(s, sub_s):
    return sub_s in s

def check_uppercase(s):
    return s == s.upper()


class TestNumberOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 3), 4)

    def test_subtract(self):
        self.assertEqual(subtract(1, 3), -2)


class TestStringOperations(unittest.TestCase):

    def test_check_substring(self):
        self.assertEqual(check_substring('Test123', '123'), True)
    
    def test_check_uppercase(self):
        self.assertEqual(check_uppercase('TEST123'), True)


def make_suites():
    number_operations_tests = [
        TestNumberOperations('test_add'),
        TestNumberOperations('test_subtract')
    ]
    string_operations_tests = [
        TestStringOperations('test_check_substring'),
        TestStringOperations('test_check_uppercase')
    ]

    return unittest.TestSuite(tests=number_operations_tests), unittest.TestSuite(tests=string_operations_tests)
    
if __name__=='__main__':
    num_operations_suite, string_operations_suite = make_suites()
    runner = unittest.TextTestRunner(verbosity=2)
    print('***Running Number Operations Test Suite***')
    runner.run(num_operations_suite)
    print('*' * 100)
    print('***Running String Operations Test Suite***')
    runner.run(string_operations_suite)