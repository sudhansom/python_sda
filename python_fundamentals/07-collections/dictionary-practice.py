import random
my_dictionary = {
    "Nepal": "Kathmandu",
    "Denmark": "Kobenhavn",
    "USA": "New York",
    "Norway": "Oslo"
}
dict2 = {
    "india": "Delhi",
    "China": "Beijing"
}
country = list(my_dictionary.keys())
print(country)
number = random.randint(0, len(my_dictionary)-1)

print(my_dictionary.popitem()) # should return the random key ... but returns the last one

print(my_dictionary)
my_dictionary.update(Denmark="copenhagen")
print(my_dictionary)
my_dictionary.update(dict2)
print(my_dictionary)
# capital_city = input(f"what is the capital city of {country[number]} :").lower()
# while True:
#
#     if capital_city == my_dictionary[country[number]].lower():
#         print("perfect")
#         break
#     elif capital_city == "exit":
#         print(f"The correct answer is : {my_dictionary[country[number]]}. ")
#         break
#     else:
#         print("Wrong answer!!! try again...")
#         capital_city = input(f"capital city of {country[number]} :").lower()

my_dict = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten"
}
a = my_dict.popitem()
print(a)
print(my_dict)
a = random.choice(list(my_dict))
print(list(my_dict))
a = my_dict.copy()
b = my_dict
print(b is my_dict)
print(a is my_dict)
a = 1
b = 0
a, b = b, a
print(a, b)


# practice
while a < 30:
    print(a)
    a, b = b, a + b
set_1 = {1, 2, 3, 4}
print(set_1)
print(type(set_1))






