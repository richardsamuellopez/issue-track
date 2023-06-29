from datetime import datetime, timedelta

class IssueTrack:
    global start_hour, end_hour, sunday, saturday
    start_hour = 9
    end_hour = 17
    sunday = 0
    saturday = 6
    def __init__(self):
        """ calc due date
        """

    def calculate_due_date(submit_date, turnaround_time):
        if turnaround_time < 0:
            return f"The turnaround time must be a positive value in hour(s)"
        elif IssueTrack.is_working_day(submit_date):
            if IssueTrack.is_working_hours(submit_date):
                return IssueTrack.reduce_turnaround_time(submit_date, turnaround_time * 60)
            else:
                return f"The submit date ({submit_date}) is outside of working hours."
        else:
            return f"The submit date ({submit_date}) is not a valid working day."

    def reduce_turnaround_time(date_time, turnaround_minutes):
        minutes_to_eod = IssueTrack.minutes_to_eod(date_time)
        if turnaround_minutes <= minutes_to_eod:
            return date_time + timedelta(minutes=turnaround_minutes)
        return IssueTrack.reduce_turnaround_time(IssueTrack.get_next_working_date(date_time), turnaround_minutes - minutes_to_eod)

    def is_working_day(date):
        day_of_week = int(date.strftime("%w"))
        if day_of_week == sunday or day_of_week == saturday:
            return False
        else:
            return True

    def is_working_hours(date):
        hour_of_day = int(date.strftime("%H"))
        if hour_of_day >= start_hour and hour_of_day < end_hour:
            return True
        else:
            return False

    def get_next_working_date(date):
        day_of_week = int(date.strftime("%w"))
        if day_of_week == 6:
          date_increment = 2
        elif day_of_week == 5:
          date_increment = 3
        else:
          date_increment = 1
        return date.replace(hour=start_hour, minute=0) + timedelta(date_increment)

    def minutes_to_eod(date_time):
        submit_hour = int(date_time.strftime("%H"))
        submit_minute = int(date_time.strftime("%M"))
        return (end_hour - submit_hour) * 60 - submit_minute

if __name__ == '__main__':
    now = datetime.now()

    dueDate = IssueTrack.calculate_due_date(now, 2)
    print(dueDate)
