# take only 3 parameters and split it
import sys
my_dict = {}
countries = sys.argv[1:]
countries = countries[0].split(",")
print(countries)
for i in range(len(countries)):
    country_capital = countries[i].split("-")
    my_dict[country_capital[0]] = country_capital[1]

print(my_dict)
print("-"*20)
for key, value in my_dict.items():
    print(key, "->", value)
print("-"*20)

