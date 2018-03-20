# - *- coding: utf- 8 - *-
"""Exercise 15: Distance Units
In this exercise, you will create a program that begins by reading a measurement
in feet from the user. Then your program should display the equivalent distance in
inches, yards and miles. Use the Internet to look up the necessary conversion factors
if you don’t have them memorized."""

## Solution:

# ask the user to enter the value in feet
feet = float(input("Enter the distance (in feet): "))

# convert the value from feet to inches, yard and miles
inch = feet * 12  # 1 foot = 12 inch
yard = feet * 0.333   # 1 foot = 0.333 yard
mile = feet / 5280  # i mile = 5280 feet

# Display the result
print("The equivalent distance in inches, yards and miles are {:.2f} inches, {:.3f} yards and {:.3f} miles".format(
inch, yard, mile))

