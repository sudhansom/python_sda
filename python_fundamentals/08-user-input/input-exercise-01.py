# create a dictionary
my_dict = dict()
print(type(my_dict))
# promt a user to insert countru and the capital
for i in range(3):
    country = input("Enter the country name: ")
    capital = input("Enter its capital: ")
    my_dict[country] = capital

print(f"Dictionary containing all the given country and capitals : {my_dict}")