"""Exercise 19: Free Fall
Create a program that determines how quickly an object is traveling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).
Because the object is dropped its initial speed is 0 m/s. Assume
that the acceleration due to gravity is 9.8 m/s^2 . You can use the formula vf = squre root of(vi^2 + 2ad) to compute the
final speed, vf , when the initial speed, vi , acceleration, a, and distance, d, are known."""

## Solution:

# import the sqrt function from the math module
from math import sqrt

# ask the user to enter the height from where the object is dropped
d = float(input("Enter the height(in merters) from where the object is dropped: "))
vi = 0  # initial speed is zero
a = 9.8 # accelaration due to gravity is 9.8

# calculate the final speed
vf = sqrt(vi*vi+2*a*d)

# Display the result
print("The speed at which the object is travelling when it hits the ground is {:.2f} m/s".format(vf))
