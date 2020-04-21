import sys
my_dict = {}
country_list = sys.argv[1:]
for i in range(0, len(country_list), 2):
    my_dict[country_list[i]] = country_list[i+1]

print(f"\nDictionary details : \n\n {my_dict}")
