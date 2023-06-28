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

    def calculate_due_date(start, turnAroundTime):
        return turnAroundTime

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

    def is_before_working_hours(date):
        hour_of_day = int(date.strftime("%H"))
        if hour_of_day < start_hour:
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
        return date + timedelta(date_increment)

if __name__ == '__main__':
    now = datetime.now()

    dueDate = IssueTrack.calculate_due_date(now, 2)
    print(dueDate)