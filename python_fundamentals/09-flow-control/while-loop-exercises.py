number = int(input("Enter the number: "))
n = 0
while n < number:
    print(" " * (number-n), end='')
    print("*" * (2*n-1), end='')
    print(" "*(number-n))
    n += 1
print("abc", end='')
n = 1
while n < number:
    i = 1
    while i < n:
        print(i, end='')
        i += 1
    n += 1
    print("")

n = 0
while n < number:
    i = 0
    while i <= n:
         print(n+1+i, end='')
         i += 1
    n += 1
    print("")

print("hello.....", end='')
