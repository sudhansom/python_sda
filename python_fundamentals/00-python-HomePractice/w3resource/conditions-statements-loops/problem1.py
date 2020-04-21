"""
Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700
(both included).

"""

result = []
for num_ in range(1500, 2701):
    if num_ % 7 == 0 and num_ % 5 == 0:
        result.append(str(num_))

print(','.join(result))
