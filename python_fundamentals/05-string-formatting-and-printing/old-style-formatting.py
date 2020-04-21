# old style printing by using %

name = "sudhan"
last_name = "poudel"
age = 38
a = 9
b = 3
print("%s is a nice guy of age: %d" % (name, age))

# printf - style
print("%(name)s is a guy of age %(age)d" % {"name":name, "age":age})

# takes the values from the dictionary , order does not matter
print("%(name)s is a guy of age %(age)d" % {"age":age, "name":name})

# by calling .format() method

print("hey {} , are you now {}?".format(name, age))

print("hey {1} , are you now {0}?".format(age, name))

# f - format

print(f"hi {name} {last_name}, now you are {age} years old.")
print(f"{a} times {b} is {a*b} ")