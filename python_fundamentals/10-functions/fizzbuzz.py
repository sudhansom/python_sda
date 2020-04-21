user_input = int(input("Enter the number: "))
# for num in range(1, user_input):
#     if num % 3 == 0:
#         if num % 5 ==0:
#             print("FizzBuzz")
#         else:
#             print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

for num in range(1, user_input):
    output = ""
    if num % 3 == 0:
        output += "Fizz"
    if num % 5 == 0:
        output += "Buzz"
    elif num % 3 != 0:
        output = num
    print(output)

