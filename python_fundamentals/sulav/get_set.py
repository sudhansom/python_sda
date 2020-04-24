class Person:
    pass

person = Person()

person_dict = {'name': 'sudhan', 'l_name': 'poudel'}

first_key = 'age'
first_value = "38"

person.first_key = first_value

print(person.first_key)


person_dict[first_key] = first_value

setattr(person, first_key, first_value)

for key, value in person_dict.items():
    setattr(person, key, value)

print(getattr(person, 'name'))


