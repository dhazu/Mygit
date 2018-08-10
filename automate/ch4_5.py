"""Say you have a list of lists where each value in the inner lists is a one-character
string, like this:
    grid  = [['.', '.', '.', '.', '.', '.'],
             ['.', '0', '0', '.', '.', '.'],
             ['0', '0', '0', '0', '.', '.'],
             ['0', '0', '0', '0', '0', '.'],
             ['.', '0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0', '.'],
             ['0', '0', '0', '0', '.', '.'],
             ['.', '0', '0', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.']]

Copy the previous grid value, and write code that uses it to print the image.

..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....

"""
## Solution:
import copy             # import the copy module to copy the argument
def makeshap(arg):      # define the function
    for i in range(6):  # create a outer loop in the lenth of number of character in a list
        for j in range(len(arg)):   # create the inner loop 
            print(arg[j][i], end = '')  
        print()         # print a new line everytime after the inner loop
                   
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

x = copy.deepcopy(grid)     # copy the list value
makeshap(x)                 # call the function
