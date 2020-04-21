# creating a dictionary
my_dictionary = {1: "one", 2: "two", 3: "three"}
# finding the length of the dictionary
print(f"the length of the dictionary is : {len(my_dictionary)} .")
# add a key to the dictionary
my_dictionary[4] = "four"
my_dictionary.__setitem__(5, "five")
print(my_dictionary)
# printing one key - value of the dictionary
print(my_dictionary[2])
print(my_dictionary.get(11))
print(my_dictionary.__getitem__(5))
print(my_dictionary.get(6, "this does not exist in the dictionary"))
# using pop function
my_dictionary.pop(2)
print(my_dictionary)
# creating a new dictionary
new_dict = {0: "zero"}
merge_dictionary = {**my_dictionary, **new_dict}
# my_dictionary.update(new_dict)
print(my_dictionary)
print(f"after merging :{merge_dictionary}")
# chaining the dictionaries
import collections
chain = collections.ChainMap(my_dictionary, new_dict)
print(f"chain of two dictionary is: {dict(chain)}")

# clearing the dictionary
my_dictionary.clear()
print(my_dictionary)



