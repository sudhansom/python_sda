# create a dictionary of 7 days in a week
seven_days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}
day = int(input("Enter the day in a week 1 to 7 : "))
if day < 1:
    print(f"Day can not be {day}. It starts from 1.")
elif day > 7:
    print(f"there are only 7 days in a week. But you entered {day}.")
else:
    print(f"you entered the day {day} which is {seven_days[day]}")
