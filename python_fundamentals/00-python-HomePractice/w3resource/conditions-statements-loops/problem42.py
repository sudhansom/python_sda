"""
Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.

"""
list_ = []
while True:
    user_input = int(input("Enter a number"))
    if user_input == 0:
        break
    else:
        list_.append(user_input)

print(f"Sum is : {sum(list_)}")
print(f"Average is : {sum(list_)/len(list_)}")
