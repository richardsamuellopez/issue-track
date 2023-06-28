from datetime import datetime, timedelta
import unittest

from app import IssueTrack

class TestCalculateDueDate(unittest.TestCase):
  now = datetime.now()

  global monday, hour_0, hour_1, hour_2, hour_3, hour_4, hour_5, hour_6, hour_7, hour_8, hour_9, hour_10, hour_11, hour_12, hour_13, hour_14, hour_15, hour_16, hour_17, hour_18, hour_19, hour_20, hour_21, hour_22, hour_23
  monday = datetime(2023, 6, 26, 13)
  hour_0 = datetime(2023, 6, 25)
  hour_1 = datetime(2023, 6, 25, 1)
  hour_2 = datetime(2023, 6, 25, 2)
  hour_3 = datetime(2023, 6, 25, 3)
  hour_4 = datetime(2023, 6, 25, 4)
  hour_5 = datetime(2023, 6, 25, 5)
  hour_6 = datetime(2023, 6, 25, 6)
  hour_7 = datetime(2023, 6, 25, 7)
  hour_8 = datetime(2023, 6, 25, 8)
  hour_9 = datetime(2023, 6, 25, 9)
  hour_10 = datetime(2023, 6, 25, 10)
  hour_11 = datetime(2023, 6, 25, 11)
  hour_12 = datetime(2023, 6, 25, 12)
  hour_13 = datetime(2023, 6, 25, 13)
  hour_14 = datetime(2023, 6, 25, 14)
  hour_15 = datetime(2023, 6, 25, 15)
  hour_16 = datetime(2023, 6, 25, 16)
  hour_17 = datetime(2023, 6, 25, 17)
  hour_18 = datetime(2023, 6, 25, 18)
  hour_19 = datetime(2023, 6, 25, 19)
  hour_20 = datetime(2023, 6, 25, 20)
  hour_21 = datetime(2023, 6, 25, 21)
  hour_22 = datetime(2023, 6, 25, 22)
  hour_23 = datetime(2023, 6, 25, 23)

  def test_is_before_working_hours(self):
    self.assertTrue(IssueTrack.is_before_working_hours(hour_0))
    self.assertTrue(IssueTrack.is_before_working_hours(hour_1))
    self.assertTrue(IssueTrack.is_before_working_hours(hour_2))
    self.assertTrue(IssueTrack.is_before_working_hours(hour_3))
    self.assertTrue(IssueTrack.is_before_working_hours(hour_4))
    self.assertTrue(IssueTrack.is_before_working_hours(hour_5))
    self.assertTrue(IssueTrack.is_before_working_hours(hour_6))
    self.assertTrue(IssueTrack.is_before_working_hours(hour_7))
    self.assertTrue(IssueTrack.is_before_working_hours(hour_8))
    self.assertFalse(IssueTrack.is_before_working_hours(hour_9))
    self.assertFalse(IssueTrack.is_before_working_hours(hour_10))
    self.assertFalse(IssueTrack.is_before_working_hours(hour_11))
    self.assertFalse(IssueTrack.is_before_working_hours(hour_12))
    self.assertFalse(IssueTrack.is_before_working_hours(hour_13))
    self.assertFalse(IssueTrack.is_before_working_hours(hour_14))
    self.assertFalse(IssueTrack.is_before_working_hours(hour_15))
    self.assertFalse(IssueTrack.is_before_working_hours(hour_16))
    self.assertFalse(IssueTrack.is_before_working_hours(hour_17))
    self.assertFalse(IssueTrack.is_before_working_hours(hour_18))
    self.assertFalse(IssueTrack.is_before_working_hours(hour_19))
    self.assertFalse(IssueTrack.is_before_working_hours(hour_20))
    self.assertFalse(IssueTrack.is_before_working_hours(hour_21))
    self.assertFalse(IssueTrack.is_before_working_hours(hour_22))
    self.assertFalse(IssueTrack.is_before_working_hours(hour_23))

  def test_is_working_hours(self):
    self.assertFalse(IssueTrack.is_working_hours(hour_0))
    self.assertFalse(IssueTrack.is_working_hours(hour_1))
    self.assertFalse(IssueTrack.is_working_hours(hour_2))
    self.assertFalse(IssueTrack.is_working_hours(hour_3))
    self.assertFalse(IssueTrack.is_working_hours(hour_4))
    self.assertFalse(IssueTrack.is_working_hours(hour_5))
    self.assertFalse(IssueTrack.is_working_hours(hour_6))
    self.assertFalse(IssueTrack.is_working_hours(hour_7))
    self.assertFalse(IssueTrack.is_working_hours(hour_8))
    self.assertTrue(IssueTrack.is_working_hours(hour_9))
    self.assertTrue(IssueTrack.is_working_hours(hour_10))
    self.assertTrue(IssueTrack.is_working_hours(hour_11))
    self.assertTrue(IssueTrack.is_working_hours(hour_12))
    self.assertTrue(IssueTrack.is_working_hours(hour_13))
    self.assertTrue(IssueTrack.is_working_hours(hour_14))
    self.assertTrue(IssueTrack.is_working_hours(hour_15))
    self.assertTrue(IssueTrack.is_working_hours(hour_16))
    self.assertFalse(IssueTrack.is_working_hours(hour_17))
    self.assertFalse(IssueTrack.is_working_hours(hour_18))
    self.assertFalse(IssueTrack.is_working_hours(hour_19))
    self.assertFalse(IssueTrack.is_working_hours(hour_20))
    self.assertFalse(IssueTrack.is_working_hours(hour_21))
    self.assertFalse(IssueTrack.is_working_hours(hour_22))
    self.assertFalse(IssueTrack.is_working_hours(hour_23))

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

  # def test_get_next_working_day(self):

  def test_dueToday(self):
    dueDate = IssueTrack.calculate_due_date(monday, 2)
    dueToday = datetime(2023, 6, 26, 15)

    self.assertEqual(dueDate, 2, f'{dueDate} equals {dueToday}')

if __name__ == '__main__':
  unittest.main()