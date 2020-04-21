# write a function that returns the biggest of all the three given numbers

def max_of_three(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c



print(max_of_three(3, 7, 3))