"""
    Write a Python program to count the number of even and odd numbers from a series of numbers.
    Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4

"""

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_number = 0
odd_number = 0
for item in numbers:
    if item % 2 == 0:
        even_number += 1
    else:
        odd_number += 1

print(f"Number of even number : {even_number} \nNumber of odd numbers : {odd_number}")
