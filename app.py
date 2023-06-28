from datetime import datetime

class IssueTrack:
    def __init__(self):
        """ calc due date
        """
    def calculate_due_date(start, turnAroundTime):
        return turnAroundTime
    def is_working_day(date):
        day_of_week = int(date.strftime("%w"))
        if day_of_week == 0 or day_of_week == 6:
            return False
        else:
            return True

if __name__ == '__main__':
    now = datetime.now()

    dueDate = IssueTrack.calculate_due_date(now, 2)
    print(dueDate)