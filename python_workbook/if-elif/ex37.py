"""Exercise 37: Name that Shape
Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message."""

## Solution:

# ask the user to enter the number of sides of the shape
no_of_side = int(input("Enter the number of sides of the shape: "))

# apply the condition and display the result
if no_of_side in range(3, 11):
    if no_of_side == 3:
        print("The shape is called a triangle")
    elif no_of_side == 4:
        print("The shape is called a ractangle")
    elif no_of_side == 5:
        print("The shape is called a pentagon")
    elif no_of_side == 6:
        print("The shape is called a hexagon")
    elif no_of_side == 7:
        print("The shape is called a heptagon or sometimes reffered as septagon")
    elif no_of_side == 8:
        print("The shape is called an octagon")
    elif no_of_side == 9:
        print("The shape is called a nonagon")
    elif no_of_side == 10:
        print("The shape is called a decagon")
else:
    print("Enter a value in the range 3-10")

