import calendar
import datetime

# 🗓️ Display all month names
print("Months of the Year:")
for month_num in range(1, 13):
    print(f"{month_num}: {calendar.month_name[month_num]}")

# 🔍 Find the month name of a given date
date_input = input("\nEnter a date (YYYY-MM-DD): ")
year, month, day = map(int, date_input.split('-'))
date_obj = datetime.date(year, month, day)

month_name = calendar.month_name[date_obj.month]
print(f"The month for {date_input} is: {month_name}")
