# - *- coding: utf- 8 - *-
"""Exercise 23: Area of a Regular Polygon
A polygon is regular if its sides are all the same length and the angles between all of
the adjacent sides are equal. The area of a regular polygon can be computed using
the following formula, where s is the length of a side and n is the number of sides:"""
# area = (n*s^2)/(4*tan(pi/n))
"""Write a program that reads s and n from the user and then displays the area of a
regular polygon constructed from these values."""

## Solution:
# import required trigonometric function from the math module
from math import pi, tan

# ask the user to enter the length of the side and no sides of the polygon 
n = int(input("Enter the number of sides of the polygon: "))
s = float(input("Enter the length of the each side of the polygon(in cms): "))

# Calculate the area of the polygon
area = (n*s*s)/(4*tan(pi/n))

# Display the result
print("The area of the polygon is {:.2f} squre cms".format(area))

