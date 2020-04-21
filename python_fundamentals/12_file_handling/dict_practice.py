import csv

with open('textfiles/abc.csv', 'r') as f:
    f = csv.DictReader(f, delimiter=',')

    list_dict = [row for row in f]

list_key = []

print(list_dict[0])
for key in list_dict[0]:
    list_key.append(key)
list_value = [[] for i in range(len(list_dict))]
"""
for items in list_dict:
    i = 0
    for key, value in items.items():
        list_value[i].append(value)
        i += 1
"""
for i, items in enumerate(list_dict):
    for j in range(len(list_key)):
        list_value[i].append(list_dict[i][list_key[j]])



print(list_value)


with open('textfiles/new_abc.csv', 'w') as f:
    fieldnames = list_key
    f = csv.DictWriter(f, fieldnames=fieldnames, delimiter=',')
    f.writeheader()
    for row in list_dict:
        f.writerow(row)



