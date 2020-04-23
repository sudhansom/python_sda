dict1 = {'one': 1, 'three': 3, 'six': 6, 'four': 4, 'two': 2}


def second_element(val):
    return val[0]


s_dict1 = sorted(dict1.items(), key=second_element)
dict2 = dict(s_dict1)
print(type(s_dict1), "--> ", s_dict1)
print(type(s_dict1[-1]), "--> ", s_dict1[-1])
print(type(dict1.values()), "--> ", dict1.values())
print(dict2)
