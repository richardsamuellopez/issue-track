from datetime import datetime, timedelta
import unittest

from app import IssueTrack

class TestCalculateDueDate(unittest.TestCase):
  now = datetime.now()

  global sunday, monday, tuesday, wednesday, thursday, friday, saturday
  sunday = datetime(2023, 6, 25)
  monday = sunday + timedelta(1)
  tuesday = sunday + timedelta(2)
  wednesday = sunday + timedelta(3)
  thursday = sunday + timedelta(4)
  friday = sunday + timedelta(5)
  saturday = sunday + timedelta(6)
  global hour_0, hour_1, hour_2, hour_3, hour_4, hour_5, hour_6, hour_7, hour_8, hour_9, hour_10, hour_11, hour_12, hour_13, hour_14, hour_15, hour_16, hour_17, hour_18, hour_19, hour_20, hour_21, hour_22, hour_23
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
    self.assertFalse(IssueTrack.is_working_day(sunday))
    self.assertTrue(IssueTrack.is_working_day(monday))
    self.assertTrue(IssueTrack.is_working_day(tuesday))
    self.assertTrue(IssueTrack.is_working_day(wednesday))
    self.assertTrue(IssueTrack.is_working_day(thursday))
    self.assertTrue(IssueTrack.is_working_day(friday))
    self.assertFalse(IssueTrack.is_working_day(saturday))

  def test_get_next_working_date(self):
    next_monday = monday + timedelta(7)
    self.assertEqual(IssueTrack.get_next_working_date(sunday), monday.replace(hour=9))
    self.assertEqual(IssueTrack.get_next_working_date(monday), tuesday.replace(hour=9))
    self.assertEqual(IssueTrack.get_next_working_date(tuesday), wednesday.replace(hour=9))
    self.assertEqual(IssueTrack.get_next_working_date(wednesday), thursday.replace(hour=9))
    self.assertEqual(IssueTrack.get_next_working_date(thursday), friday.replace(hour=9))
    self.assertEqual(IssueTrack.get_next_working_date(friday), next_monday.replace(hour=9))
    self.assertEqual(IssueTrack.get_next_working_date(saturday), next_monday.replace(hour=9))

  def test_reduce_turn_around_time(self):
    start_time = datetime(2023, 6, 26, 11, 23)

    self.assertEqual(IssueTrack.reduce_turn_around_time(start_time, 120), start_time + timedelta(hours=2))
    self.assertEqual(IssueTrack.reduce_turn_around_time(start_time, 8 * 60), start_time + timedelta(days=1))

  def test_minutes_to_eod(self):
    start_time = datetime(2023, 6, 26, 11, 23)
    self.assertEqual(IssueTrack.minutes_to_eod(start_time), 337)

  def test_calculate_due_date_non_working_day(self):
    self.assertEqual(IssueTrack.calculate_due_date(saturday, 0), f"The submit date ({saturday}) is not a valid working day.")
    self.assertEqual(IssueTrack.calculate_due_date(sunday, 0), f"The submit date ({sunday}) is not a valid working day.")

  def test_calculate_due_date_outside_of_business_hours(self):
    self.assertEqual(IssueTrack.calculate_due_date(monday, 0), f"The submit date ({monday}) is outside of working hours.")
    monday_at_close = monday.replace(hour=17)
    self.assertEqual(IssueTrack.calculate_due_date(monday_at_close, 0), f"The submit date ({monday_at_close}) is outside of working hours.")

  def test_calculate_due_date_in_one_week(self):
    date = datetime(2023, 6, 26, 11, 11)
    self.assertEqual(IssueTrack.calculate_due_date(date, 8 * 5), date + timedelta(days=7))

  def test_calculate_due_date_tuesday_to_thurday(self):
    date = datetime(2023, 6, 27, 14, 12)
    self.assertEqual(IssueTrack.calculate_due_date(date, 16), date + timedelta(days=2))

if __name__ == '__main__':
  unittest.main()
