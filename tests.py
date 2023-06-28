from datetime import datetime, timedelta
import unittest

from app import IssueTrack

class TestCalculateDueDate(unittest.TestCase):
  now = datetime.now()

  global monday 
  monday = datetime(2023, 6, 26, 13)

  # def test_isWorkingHours(self):

  def test_is_working_day(self):
    sunday = datetime(2023, 6, 25)
    day_0 = sunday
    day_1 = sunday + timedelta(1)
    day_2 = sunday + timedelta(2)
    day_3 = sunday + timedelta(3)
    day_4 = sunday + timedelta(4)
    day_5 = sunday + timedelta(5)
    day_6 = sunday + timedelta(6)

    self.assertFalse(IssueTrack.is_working_day(day_0))
    self.assertTrue(IssueTrack.is_working_day(day_1))
    self.assertTrue(IssueTrack.is_working_day(day_2))
    self.assertTrue(IssueTrack.is_working_day(day_3))
    self.assertTrue(IssueTrack.is_working_day(day_4))
    self.assertTrue(IssueTrack.is_working_day(day_5))
    self.assertFalse(IssueTrack.is_working_day(day_6))

  # def test_getNextWorkingDay(self):

  def test_dueToday(self):
    dueDate = IssueTrack.calculate_due_date(monday, 2)
    dueToday = datetime(2023, 6, 26, 15)

    self.assertEqual(dueDate, 2, f'{dueDate} equals {dueToday}')

if __name__ == '__main__':
  unittest.main()