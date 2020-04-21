"""
Write a Python program to construct the following pattern, using a nested for loop.

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

"""
user_input = int(input("Enter the height of the pyramid : ").strip())
n = int(user_input / 2)
for i in range(n):
    for j in range(i):
        print('*', end="")
    print("")
for i in range(n, 0, -1):
    for j in range(i):
        print('*', end="")
    print("")

# using only one loop:

for i in range(user_input):
    if i < user_input/2:
        print(i * '*', end='')
    else:
        print((user_input-i) * '*', end='')
    print("")
