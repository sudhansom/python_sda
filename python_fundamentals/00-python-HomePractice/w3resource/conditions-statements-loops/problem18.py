"""
Write a Python program to print alphabet pattern 'D'. Go to the editor
Expected Output:

 ****
 *   *
 *   *
 *   *
 *   *
 *   *
 ****

"""

length = int(input("Enter the length: ").strip())
breadth = int(input("Enter the breadth: ").strip())
for i in range(length):
    for j in range(breadth):
        if (i == 0 and j == breadth - 1) or (i == length - 1 and j == breadth - 1):
            print(' ', end='')
        elif i == 0 or j == 0 or i == length - 1 or j == breadth - 1:
            print("*", end='')
        else:
            print(" ", end='')
    print('')
