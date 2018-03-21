"""Exercise 16: Area and Volume
Write a program that begins by reading a radius, r , from the user. The program will
continue by computing and displaying the area of a circle with radius r and the
volume of a sphere with radius r . Use the pi constant in the math module in your
calculations."""

## Solution:

# import the pi function from the math module
from math import pi

# ask the user to enter the radius 
r = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle and volume of the sphere with the radius r
area = pi*r*r
vol = (4/3) * pi * (r ** 3)

# Display the result
print("""The area of the circle and volume of the sphere having radius {} unit are 
{:.2f} squre unit and {:.2f} qubic unit""".format(r, area, vol))
