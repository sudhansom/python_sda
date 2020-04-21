# assigning few names to the list ' users '
users = ["user1", "userchris", "user2", "admin"]
# printing the slice containing only " user2 "
print(users[2:3])
# printing the list except the first one
print(users[1:])
# printing the slice except the last one
print(users[:-1])
# printing the slice upto the third one
print(users[:3])

print(users[1][4:][1:])
print(users[1:-1][1:-1])

str = "abcdef"
str1 = []
str1.extend(str)
print(str1)
str = "abcde"
print(f"value is {str[0:len(str)]} ")