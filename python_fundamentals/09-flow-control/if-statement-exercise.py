# user input
number = int(input("Enter a number 1 to 7 : "))
if number < 1:
    print("no negative days or the day starts only from 1 ...")
elif number == 1:
    print("you choose Monday.")
elif number > 7:
    print("there are only 7 days in a week. ")
else:
    print("not Monday . Right ???")

# homework --- make a dictionary.. of all the days like 1 _-> Sunday .... and ask the user enter the number...