list_month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
# user input
month = input("Enter month:: ").title()
position = list_month.index(month) + 1
number_of_days = 31
print(position)

if position == 2:
    number_of_days = 28
elif (position <= 7 and position % 2 == 0) or (position > 7 and position % 2 == 1):
    number_of_days = 30


print(f"number of days in month {month} is {number_of_days}")
