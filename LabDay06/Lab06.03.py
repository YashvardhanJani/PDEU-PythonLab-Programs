# 03. Suppose a date is represented as a tuple (d, m, y). Create two date tuples and find the number of days between the two dates.

from datetime import date
from dateutil.relativedelta import relativedelta  # pip install python-dateutil


def string_to_date(date_str):
    day, month, year = map(int, date_str.split('-'))
    return date(year, month, day)

def get_date_from_user():
    date_str = input("Enter the date (dd-mm-yyyy): ")
    return string_to_date(date_str)

print("Enter the first date:")
dt1 = get_date_from_user()

print("Enter the second date:")
dt2 = get_date_from_user()

delta = dt2 - dt1
days_difference = delta.days

def days_to_years_months_days(days):
    base_date = date(2000, 1, 1)    #Create a base date (e.g., 2000-01-01)
    target_date = base_date + relativedelta(days=days)   #Add the total days to the base date
    delta = relativedelta(target_date, base_date) #Calculate the difference between the target date and base date
    return delta.years, delta.months, delta.days

print(f"Number of days between {dt1} and {dt2} : {days_difference} Days")
years, months, days = days_to_years_months_days(days_difference)
print(f"{days_difference} days = {years} years, {months} months, {days} days")