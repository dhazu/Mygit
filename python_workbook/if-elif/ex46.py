"""Exercise 46: Season from Month and Day
The year is divided into four seasons: spring, summer, fall and winter. While the
exact dates that the seasons change vary a little bit from year to year because of the
way that the calendar is constructed, we will use the following dates for this exercise:
            Season              First Day
            -----               --------
            Spring              Mar 20
            Summer              June 21
            Fall                September 21
            Winter              December 21
    Create a program that reads a month and day from the user. The user will enter
the name of the month as a string, followed by the day within the month as an
integer. Then your program should display the season associated with the date that
was entered."""

## Solution:

# ask the user to enter the month and date of the year
month = input("Enter the month: ").title()
date = int(input("Enter the day of the month: "))

# apply the condition to get the correct result and also ensure that user will always enter a valid date
if month == 'Jan':
    if 0 < date <= 31:
        print("The season is winter.")
    else:
        print("Enter a valid date")
elif month == 'Feb':
    # check whether the year is leap year or not, so that a valid date for the month feb is accepted
    answer = input("Is the year is leap year(Y/N)? ").upper()
    if answer == 'Y':
        if 0 < date <= 29:
            print("The season is winter")
        else:
            print("Enter a valid date")
    else:
        if 0 < date <= 28:
            print("The season is winter")
        else:
            print("Enter a valid date")
elif month == 'Mar':
    if date in range(1, 20):
        print("The season is winter.")
    elif date in range(20, 32):
        print("The season is Spring.")
    else:
        print("Enter a valid date.")
elif month == 'Apr' or month == 'May':
    if (month == 'Apr' and 0 < date <= 30) or (month == 'May' and 0 < date <= 31):
        print("The season is Spring.")
    else:
        print("Enter a valid date.")
elif month == 'Jun':
    if date in range (1, 21):
        print("The season is Spring.")
    elif date in range(21, 31):
        print("The season is Summer.")
    else:
        print("Enter a valid date.")
elif month == 'July' or month == 'Aug':
    if (month == 'July' and 0 < date <= 31) or (month == 'Aug' and 0 < date <= 31):
        print("The season is Summer.")
    else:
        print("Enter a valid date.")
elif month == 'Sep':
    if date in range (1, 22):
        print("The season is Summer.")
    elif date in range(22, 31):
        print("The season is Fall.")
    else:
        print("Enter a valid date.")
elif month == 'Oct' or month == 'Nov':
    if (month == 'Oct' and 0 < date <= 31) or (month == 'Nov' and 0 < date <= 30):
        print("The season is Fall.")
    else:
        print("Enter a valid date.")
elif month == 'Dec':
    if date in range (1, 21):
        print("The season is Fall.")
    elif date in range(21,32):
        print("The season is Winter.")
    else:
        print("Enter a valid date.")
