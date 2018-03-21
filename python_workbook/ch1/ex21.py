"""Exercise 21: Area of a Triangle
The area of a triangle can be computed using the following formula, where b is the
length of the base of the triangle, and h is its height:
area = (b*h)/2
    Write a program that allows the user to enter values for b and h. The program
should then compute and display the area of a triangle with base length b and height h."""

##Solution:
# ask the user to enter the base length and height of the triangle
b = float(input("Enter the base length of the triagle(in cms): "))
h = float(input("Enter the height of the triangle (in cms): "))

# Calculate the area of the triangle
area = (b*h)/2

# Display the result
print("""
The area of the triangle having the base {:.2f} cms and {:.2f} cms height is {:.2f} squre cms""".format(
b,h,area))
