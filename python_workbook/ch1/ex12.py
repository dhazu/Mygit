"""Exercise 12: Distance Between Two Points on Earth
The surface of the Earth is curved, and the distance between degrees of longitude
varies with latitude. As a result, finding the distance between two points on the surface
of the Earth is more complicated than simply using the Pythagorean theorem.
Let (t 1 , g 1 ) and (t 2 , g 2 ) be the latitude and longitude of two points on the Earth’s
surface. The distance between these points, following the surface of the Earth, in
kilometers is:
distance = 6371.01 × arccos(sin(t 1 ) × sin(t 2 ) + cos(t 1 ) × cos(t 2 ) × cos(g 1 − g 2 ))"""
# The value 6371.01 in the previous equation wasn’t selected at random. It is the average radius of the Earth in kilometers.
"""Create a program that allows the user to enter the latitude and longitude of two
points on the Earth in degrees. Your program should display the distance between
the points, following the surface of the earth, in kilometers."""
#Hint: Python’s trigonometric functions operate in radians. As a result, you will
#need to convert the user’s input from degrees to radians before computing the
#distance with the formula discussed previously. The math module contains a
#function named radians which converts from degrees to radians.

##Solution: 
# import trigonometric functions from math module
from math import acos, sin, cos, radians

# ask the user for inputs the points
t1 = float(input("Enter the latitude of the first point: "))
g1 = float(input("Enter the longitude of the first point: "))
t2 = float(input("Enter the latitude of the second point: "))
g2 = float(input("Enter the longitude of the second point: "))

# Now convert the input value from degrees to radians
t1_r = radians(t1)
g1_r = radians(g1)
t2_r = radians(t2)
g2_r = radians(g2)

# Now computer the distance between these two points
d = 6371.01 * acos(sin(t1_r) * sin(t2_r) + cos(t1_r) * cos(t2_r) * cos(g1-g2))
 
print("The distance between these two points on earth's surface is {:.3f} km".format(d))
