# write a function which prints out a rectangle made of character and wall size defined by user

def print_rectangle(size, char='#'):
    for i in range(size):
        print(char * size)

print_rectangle(10, 'd')

help(print_rectangle)
