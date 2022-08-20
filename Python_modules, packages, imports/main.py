import application
from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime


def get_date():
    date_today = datetime.today()
    day_today_formatted = date_today.strftime("%A, %d %B %Y %I:%I%p")
    return day_today_formatted


if __name__ == '__main__':
    print(get_date())
    application.salary.calculate_salary()
    application.db.people.get_employees()
