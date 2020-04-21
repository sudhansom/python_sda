"""
Write a Python program that accepts a string and calculate the number of digits and letters.
Sample Data : Python 3.2
Expected Output :
Letters 6
Digits 2

"""
string_ = input("Enter a string").strip()
num_letters = 0
num_digits = 0
for _ in string_:
    if _.isalpha():
        num_letters += 1
    elif _.isdigit():
        num_digits += 1

print(f"Letters : {num_letters}")
print(f"Digits : {num_digits}")