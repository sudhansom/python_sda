"""
Write a Python program to print alphabet pattern 'E'. Go to the editor
Expected Output:

 *****
 *
 *
 ****
 *
 *
 *****

"""
height = int(input("Enter the height: ").strip())
height = height + 1
width = int(height / 2) + 1

for i in range(height):
    for j in range(width):
        if i == 0 or j == 0 or i == width - 1 or i == height - 1:
            print('*', end="")
    print("")

