from application.salary import *
from application.db.people import *
from datetime import datetime


def get_date():
    date_today = datetime.today()
    day_today_formatted = date_today.strftime("%A, %d %B %Y %I:%I%p")
    return day_today_formatted


if __name__ == '__main__':
    get_date()
    calculate_salary()
    get_employees()
