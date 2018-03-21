"""Exercise 24: Units of Time
Create a program that reads a duration from the user as a number of days, hours,
minutes, and seconds. Compute and display the total number of seconds represented
by this duration."""

## Solution:

# ask the user to enter the number of days, hours, minutes and seconds
d = int(input("Enter the number of days: "))
h = int(input("Enter the number of hours: "))
m = int(input("Enter the number of minutes: "))
s = int(input("Enter the number of seconds: "))

# Calculate the total number of second
s_total = (d*24*3600)+(h*3600)+(m*60)+s

# Display the result
print("""
The total number of second in {} days, {} hrs, {} minutes and {} seconds is {} seconds""".format(
d, h, m ,s, s_total))
