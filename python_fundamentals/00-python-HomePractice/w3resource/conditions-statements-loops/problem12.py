"""
Write a Python program that accepts a sequence of lines (blank line to terminate)
as input and prints the lines as output (all characters in lower case).

"""
list_ = []
while True:
    input_string = input("Enter something : ")
    if input_string:
        list_.append(input_string)
    else:
        break

for _ in list_:
    print(_)

