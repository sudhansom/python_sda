import csv

with open('abc.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    print(" Name")
    print("---------------------------------")
    new_dict = {}
    for row in data:
        for key in row:
            if key == 'name':
                if row[key] not in new_dict:
                    new_dict[row[key]] = 0
                new_dict[row[key]] += int(row['Column5'])

for key, value in new_dict.items():
    print(f"{key} : {value}")

list1 = list(new_dict.items())


def second_element(val):
    return val[1]


list1.sort(key=second_element)

for item in list1:
    print(item)
