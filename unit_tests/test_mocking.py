'''
This is a test of the Mock object in unittest. It is mocking a call to the datetime module to 
get the current day by patching the "datetime.datetime" object.
Another test is performed by creating a custom class to get the celestial object/animal representing 
the current day of the week. We are creating a Mock object to modify the behaviour of the method
that returns the day.
'''
import unittest
from unittest.mock import Mock, patch
import datetime

def is_weekday():
    if datetime.datetime.today().weekday() > 4:
        return False
    
    return True


class WeekDay:

    day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    symbol = ['Moon', 'Mars', 'Mercury', 'Jupiter', 'Venus', 'Saturn', 'Sun']
    animal = ['Wolf', 'Tiger', 'Fox', 'Bull', 'Fish', 'Turtle', 'Lion']
    
    def set_date(self):
        return datetime.datetime.today().weekday()

    def get_day_representation(self):
        current_day = self.set_date()
        today = f"{self.day[current_day]} - {self.symbol[current_day]} - {self.animal[current_day]}"
        return today
    

class TestWeekDayRepresentation(unittest.TestCase):

    def setUp(self):
        self.day = WeekDay()

    def tearDown(self):
        del self.day

    def test_is_monday(self):
        self.day.set_date = Mock(return_value=0)
        self.assertEqual(self.day.get_day_representation(), 'Monday - Moon - Wolf')

    def test_is_tuesday(self):
        self.day.set_date = Mock(return_value=1)
        self.assertEqual(self.day.get_day_representation(), 'Tuesday - Mars - Tiger')

    def test_is_sunday(self):
        self.day.set_date = Mock(return_value=6)
        self.assertEqual(self.day.get_day_representation(), 'Sunday - Sun - Lion')


class TestIsWeekday(unittest.TestCase):
    
    @patch('datetime.datetime')
    def test_is_weekday(self, mock_datetime):
        mock_datetime.today.return_value = datetime.date(2025, 12, 24)
        self.assertTrue(is_weekday())

    @patch('datetime.datetime')
    def test_is_weekend(self, mock_datetime):
        mock_datetime.today.return_value = datetime.date(2025, 12, 28)
        self.assertFalse(is_weekday())



if __name__=='__main__':
    unittest.main(verbosity=2)
