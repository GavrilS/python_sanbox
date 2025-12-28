'''
This is a test of the Mock object in unittest. It is mocking a call to the datetime module to 
get the current day.
'''
import unittest
from unittest.mock import Mock, patch
import datetime

def is_weekday():
    if datetime.datetime.today().weekday() > 4:
        return False
    
    return True


class TestIsWeekday(unittest.TestCase):
    
    @patch('datetime.datetime')
    def test_is_weekday(self, mock_datetime):
        mock_datetime.today.return_value = datetime.date(2025, 12, 24)
        self.assertTrue(is_weekday())



if __name__=='__main__':
    unittest.main(verbosity=2)
    