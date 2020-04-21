"""
Write a Python program to convert month name to a number of days.
Expected Output:

List of months: January, February, March, April, May, June, July, August, September, October, November, December
Input the name of Month: February
No. of days: 28/29 days

"""
list_month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
# user input
month = input("Enter month:: ").title()
position = list_month.index(month) + 1
number_of_days = 31

if position == 2:
    number_of_days = '28 / 29'
elif (position <= 7 and position % 2 == 0) or (position > 7 and position % 2 == 1):
    number_of_days = 30


print(f"number of days in month {month} is {number_of_days}")

# another way :: if index is in (1, 3, 5, 7,8, 10,12) : number of days is 31 else --- 30 and 28/29 for february