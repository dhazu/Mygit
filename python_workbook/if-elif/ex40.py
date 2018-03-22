"""Exercise 40: Name that Triangle
A triangle can be classified based on the lengths of its sides as equilateral, isosceles
or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
triangle has two sides that are the same length, and a third side that is a different
length. If all of the sides have different lengths then the triangle is scalene.
    Write a program that reads the lengths of 3 sides of a triangle from the user.
Display a message indicating the type of the triangle."""

## Solution:

# ask the user to enter the length of the sides of the triangle
s1 = float(input("Enter the lenghts of the first side of the triangle: "))
s2 = float(input("Enter the lenghts of the second side of the triangle: "))
s3 = float(input("Enter the lengths of the third side of the triangle: "))

# apply the condition to check the type of the triangle
if s1 == s2 == s3:
    print("The triagle is equilaterial")
elif s1 == s2 or s1 == s3 or s2 == s3:
    print("The triagle is isosceles")
else:
    print("The triangle is scalene")
