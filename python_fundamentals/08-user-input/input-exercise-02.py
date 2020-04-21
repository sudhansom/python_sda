# create a dictionary
my_dict = dict()
print(type(my_dict))
# promt a user to insert countru and the capital
while len(my_dict)<3:
    country_capital = (input("Enter the country name and its capital seperated by a comma and space : ")).split(", ")
    my_dict[country_capital[0]] = country_capital[1]

print(f"Dictionary containing all the given country and capitals : {my_dict}")

# capitalise the first letter and strip the white spaces
word = input("enter any work").title().strip()
print(word)


import sys
print(sys.argv[1])