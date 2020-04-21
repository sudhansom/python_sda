"""
Print the following pyramid of increasing numbers.
A. User inputs the height.
B. User inputs the last number printed.
1
23
456
78910
1112131415

"""

user_input = int(input("Enter the height: ").strip())
k = 1
for i in range(user_input):
    for j in range(k, i + k):
        if k == 15:
            break
        print(j, end='')
        k = j+1
    print("")


