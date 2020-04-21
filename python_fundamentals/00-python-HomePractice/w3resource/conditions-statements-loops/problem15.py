"""
Write a Python program to check the validity of password input by users. Go to the editor
Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.

"""


def check_validity(input_string):
    flag_small_char = False
    flag_big_char = False
    flag_number = False
    sp_char = False
    for item in input_string:
        if item in ['#', '$', '@']:
            sp_char = True
        item = ord(item)  # gives a numeric value of a character
        if 122 >= item >= 97:
            flag_small_char = True
        if 90 >= item >= 65:
            flag_big_char = True
        if 48 <= item <= 57:
            flag_number = True
    return flag_small_char and flag_big_char and flag_number and sp_char


user_input = input("Enter a password")
if 16 >= len(user_input) >= 6:
    validity = check_validity(user_input)
    if validity:
        print("valid...")
    else:
        print("not valid...")
else:
    print("length should be within the range 6 to 16")
