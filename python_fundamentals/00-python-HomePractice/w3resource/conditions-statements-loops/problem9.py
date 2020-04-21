"""
Write a Python program to get the Fibonacci series between 0 to 50. Go to the editor
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34

"""
x, y = 0, 1
while x < 50:
  print(x, end=' ')
  temp = x + y
  x = y
  y = temp

# another way ... pythonic way

x, y = 0, 1
while x < 50:
    print(x, end=' ')
    x, y = y, x + y
