from collections import defaultdict

my_string = "mississippi"
dd = defaultdict(int)
for item in my_string:
    dd[item] += 1

print(dd)

dep = [
    ('sales', 'shyam'),
    ('sales', 'sudhan'),
    ('sales', "sangita"),
    ('manager','muna'),
    ('manager', 'mangal'),
    ('manager', 'manoj'),
    ('manager', 'manisha'),
    ('marketing', 'Rhythm'),
    ('marketing', 'roshan'),
    ('marketing', 'ramita'),
    ('marketing', 'rahish'),
    ('marketing', 'resham')
]
dep_dd = defaultdict(list)
print(f"dep_dd contains...: {dep_dd}")
for department, names in dep:
    dep_dd[department].append(names)
print(dep_dd)

dep_dd['director'].append('Bhuwan')
dep_dd['director'].append('som')
dep_dd['director'].append('Krishna')
print(dep_dd)

count_dep = defaultdict(int)
for department, _ in dep:
    count_dep[department] += 1

print(count_dep)
print(dep_dd)
