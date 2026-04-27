import calendar

# Input: Month Day Year (e.g., 08 05 2015)
month, day, year = map(int, input().split())

# calendar.weekday returns the day index
day_index = calendar.weekday(year, month, day)

# Get the day name in uppercase
print(calendar.day_name[day_index].upper())