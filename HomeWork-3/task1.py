import datetime


name_user = input("Enter your name: ").capitalize()
date = datetime.date.today()
day = date.isoweekday()

weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print(f"Good day {name_user}! {weekday[day-1]} is a perfect day to learn some python.")