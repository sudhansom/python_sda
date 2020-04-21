# assigning a string value to a string of length more than 10 letters
string = "hello"
reminder = len(string) % 2
print(reminder)
number_of_letters = 2
middle_index = int(len(string)/2)
start_index = middle_index - number_of_letters
end_index = middle_index + number_of_letters + reminder
result = string[start_index:end_index]
print(f"Result: {result}")


# just for a prictice
r = range(0, 20,2)
print(r)
print(r[:5])
