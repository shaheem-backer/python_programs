from datetime import datetime,date,time

dt = datetime(2023,5,23,19,9,33)

print('day is', dt.day)

print('minute is ', dt.minute)

print('todays date is ', dt.date())

print('time is ', dt.time())

print(dt.strftime('%m/%d/%Y %H:%M:%S'))  #to format datetime in string format

# when we subtract  a datetime instance from another , it produces timedelta type.

print(dt.strftime('%D %H:%M:%S')) # '%D' is shortcut for '%m/%d/%y'