"""Exercise 18: Volume of a Cylinder
The volume of a cylinder can be computed by multiplying the area of its circular
base by its height. Write a program that reads the radius of the cylinder, along with
its height, from the user and computes its volume. Display the result rounded to one
decimal place."""

##solution:

# import pi function from the math module
from math import pi

# ask the user to enter the radius and height of the cylinder
r = float(input("Enter the radius of the cylinder(in cms): "))
h = float(input("Enter the height of the cylinder(in cms): "))

# calculte the area and volume of the cylinder
area = pi*r*r
volume = area*h

# Display the result
print("The volume of the cylinder is {:.1f} qubic cms".format(volume))
