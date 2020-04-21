# write an application that prints a sum of all the even numbers between 2020 and 3030
sum1 = 0
for i in range(2020, 3031, 2):
    sum1 = sum1 + i
print(sum1)
print(i)
print(sum(list(range(2020, 3031, 2))))

