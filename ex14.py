"""Exercise 14: Height Units
Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters."""
# Hint: One foot is 12 inches. One inch is 2.54 centimeters.

## Solution:

# ask the user to enter the input
height_feet = float(input("Enter how tall are you(in feet)? "))
height_inch = float(input("Enter how tall are you(in inches)? "))

# convert the value from feet to centimeter
feet_cen = height_feet * 12 * 2.54
inch_cen = height_inch * 2.54

# Display the result
print("The equivalent height in centimeter are {:.2f} cms and {:.2f} cms".format(feet_cen, inch_cen)) 
