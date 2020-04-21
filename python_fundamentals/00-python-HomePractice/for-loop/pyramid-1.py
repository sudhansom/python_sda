# Print the following pyramid of numbers increasing row-wise. User inputs the height.

user_input = int(input("Enter the height: ").strip())
print(user_input)
for i in range(user_input):
    for j in range(1, i+1):
        print(j, end='')
    print("")
