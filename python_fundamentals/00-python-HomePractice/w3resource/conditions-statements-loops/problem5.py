"""
Write a Python program that accepts a word from the user and reverse it.

"""

user_input = input("Enter a word to be reversed: ")
print(f" Reversed string is : {user_input[::-1]}")

# another way
new_string = ''
for i in range(len(user_input)):
    new_string += user_input[len(user_input) -1 - i]

print("second way : ", new_string)

new_string = ''
for i in range(len(user_input) - 1, -1, -1):
    new_string += user_input[i]

print("Third way :", new_string)

print(f"Fourth way is : {user_input[len(user_input)::-1]}")

print(f"Fifth way is : {''.join(reversed(user_input))}")

print("""
This is a powerful technique that takes advantage of Python’s iterator protocol. 
This technique reverses a string using reverse iteration with the reversed() built-in function 
to cycle through the elements in the string in reverse order 
and then use .join() method to merge all of the characters resulting from the reversed iteration into a new string.

""")


