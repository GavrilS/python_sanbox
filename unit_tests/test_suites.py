import unittest

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def check_substring(s, sub_s):
    return sub_s in s

def check_uppercase(s):
    return s == s.uppercase()


class TestSuitesOfTests(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 3), 4)

    def test_subtract(self):
        self.assertEqual(subtract(1, 3), -2)

    def test_check_substring(self):
        self.assertEqual(check_substring('Test123', '123'), True)
    
    def test_check_uppercase(self):
        self.assertEqual(check_uppercase('TEST123'), True)

    
if __name__=='__main__':
    pass