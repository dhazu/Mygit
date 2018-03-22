"""Exercise 44: Date to Holiday Name
Canada has three national holidays which fall on the same dates each year.
        Holiday                     Date
        -------                     ----
        New year’s day              January 1
        Canada day                  July 1
        Christmas day               December 25
        
    Write a program that reads a month and day from the user. If the month and day
match one of the holidays listed previously then your program should display the
holiday’s name. Otherwise your program should indicate that the entered month and
day do not correspond to a fixed-date holiday."""

"""Canada has two additional national holidays, Good Friday and Labour Day,
whose dates vary from year to year. There are also numerous provincial and
territorial holidays, some of which have fixed dates, and some of which have
variable dates. We will not consider any of these additional holidays in this
exercise."""

## Solution:

# ask the user to enter the month and date of the year
month = input("Enter the month of the year: ").title() 
date = int(input("Enter the date of the month: "))

# Apply the condition and get the required result
if month == 'Jan' and date == 1:
    print("It's new year's day.")
elif month == 'July' and date == 1:
    print("It's Canada day.")
elif month == 'Dec' and date == 25:
    print("It's Christmas day.")
else:
    print("Either the month or the date entered do not correspond to a fixed-day holiday.")
