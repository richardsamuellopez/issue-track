# Issue Tracker app CalculateDueDate method


### Input: Takes the submit date/time and turnaround time (in hours).
### Output: Returns the date/time when the issue is resolved.

## Run tests
`python3 tests.py`

## Rules
- Working hours are from 9AM to 5PM on every working day, Monday to Friday.
  - Receives message if submit date/time is saturday or sunday
  - Receives message if outside of working hours 
- Holidays should be ignored (e.g. A holiday on a Thursday is considered as a
working day. A working Saturday counts as a non-working day.).
  - No work to handle holidays
- The turnaround time is defined in working hours (e.g. 2 days equal 16 hours).
If a problem was reported at 2:12PM on Tuesday and the turnaround time is
16 hours, then it is due by 2:12PM on Thursday.
  - Turnaround time input is in hours, test includes this mentioned example
- A problem can only be reported during working hours. (e.g. All submit date
values are set between 9AM to 5PM.)
  - Caputed in notes for first rule
- Do not use any third-party libraries for date/time calculations (e.g. Moment.js,
Carbon, Joda, etc.) or hidden functionalities of the built-in methods.
  - Used python datetime and timedelta

