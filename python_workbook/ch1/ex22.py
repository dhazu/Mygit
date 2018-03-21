"""Exercise 22: Area of a Triangle (Again)
In the previous exercise you created a program that computed the area of a triangle
when the length of its base and its height were known. It is also possible to compute
the area of a triangle when the lengths of all three sides are known. Let s 1 , s 2 and s 3
be the lengths of the sides. Let s = (s 1 + s 2 + s 3 )/2. Then the area of the triangle
can be calculated using the following formula:
area = square root (s*(s-s1)*(s-s2)*(s-a3))         
    Develop a program that reads the lengths of the sides of a triangle from the user and
displays its area."""
## Solution:

# import the square root function from the math module
from math import sqrt

# ask the user to enter the sides of the triangle
s1 = float(input("Enter the length of the first side of the traingle(in cms): "))
s2 = float(input("Enter the length of the second side of the triangle(in cms): "))
s3 = float(input("Enter the length of the third side of the triangle(in cms): "))

# Calculate the area of the triangle
s = (s1+s2+s3)/2
area = sqrt(s*(s-s1)*(s-s2)*(s-s3))

# Display the result
print("The area of the triangle is {:.2f} squre cms".format(area))

