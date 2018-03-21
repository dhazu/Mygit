"""Exercise 38: Month Name to Number of Days
The length of a month varies from 28 to 31 days. In this exercise you will create
a program that reads the name of a month from the user as a string. Then your
program should display the number of days in that month. Display “28 or 29 days”
for February so that leap years are addressed."""

## Solution:

# ask the user to enter a month
month = input("Enter a month of the year: ").title()

# apply the condition and display the result
if month == 'Jan' or month == 'Mar' or month == 'May' or month == 'July' or month == 'Aug' or month == 'Oct' or month == 'Dec':
    print("{} has {} days".format(month, 31))
elif month == 'Feb':
    print("Is the year is a leap year(y/n)?")
    year = input().lower()
    if year == 'y':
        print("{} is has {} days".format(month, 29))
    else:
        print("{} is has {} days".format(month, 28))
else: 
    print("{} has {} days".format(month, 30))
