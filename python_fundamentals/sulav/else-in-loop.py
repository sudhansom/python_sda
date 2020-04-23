def find_people(people_list, name):
    for i, people in enumerate(people_list):
        if people == name:
            break
    else:
        return -1
    return i


name_list = ['Rhythm', 'Suchitra', 'Sudhan']

find = find_people(name_list, 'Sudhan')

print(f"the index of the given person is: {find}")
