"""Exercise 58: Next Day
    Write a program that reads a date from the user and computes its immediate successor.
For example, if the user enters values that represent 2013-11-18 then your program
should display a message indicating that the day immediately after 2013-11-18 is
2013-11-19. If the user enters values that represent 2013-11-30 then the program
should indicate that the next day is 2013-12-01. If the user enters values that represent
2013-12-31 then the program should indicate that the next day is 2014-01-01. The
date will be entered in numeric form with three separate input statements; one for
the year, one for the month, and one for the day. Ensure that your program works
correctly for leap years."""

## Solution:

# ask the user to enter the year, month and day of the month
yr = int(input("Enter the year: "))
month_no = int(input("Enter the month no of the year: "))
day = int(input("Enter the date: "))

# apply the condition for the month which have 31 days in it except Dec
if month_no == 1  or month_no == 3 or month_no == 5 or month_no == 7 or month_no == 8 or month_no == 10:
    if day in range(1, 31):      # while the day of the month from 1 to 30
        print("The immediate successor of the date is {}-{}-{}".format(yr, month_no, day+1))
    elif day == 31:
        print("The immediate successor of the date is {}-{}-0{}".format(yr, month_no+1, day-30))
    else:
        print("enter the date in between 1 to 31")
# apply the condition for the month which have 30 days in it
elif month_no == 4 or month_no == 6 or month_no == 9 or month_no == 11:     
    if day in range(1, 30):
        print("The immediate successor of the date is {}-{}-{}".format(yr, month_no, day+1))
    elif day == 30:
        print("The immediate successor of the date is {}-{}-0{}".format(yr, month_no+1, day-30)) 
    else:
        print("Enter the date between 1 to 30")               
# apply the condition for the month Feb and also check whether the year is leap year or not
elif month_no == 2:
    if yr % 400 == 0:
        if day in range (1, 29):
            print("The immediate successor of the date is {}-{}-{}".format(yr, month_no, day+1))
        elif day == 29:
            print("The immediate successor of the date is {}-{}-0{}".format(yr, month_no+1, day-28)) 
        else:
            print("Enter the date in between 1 to 29")
    elif yr % 100 == 0:
        if day in range (1, 28):
            print("The immediate successor of the date is {}-{}-{}".format(yr, month_no, day+1))
        elif day == 28:
            print("The immediate successor of the date is {}-{}-0{}".format(yr, month_no+1, day-27))
        else:
            print("Not a leap year, enter the date in between 1 to 28")
    elif yr % 4 == 0:
        if day in range(1, 29):
            print("The immediate successor of the date is {}-{}-{}".format(yr, month_no, day+1))
        elif day == 29:
            print("The immediate successor of the day is {}-{}-0{}".format(yr, month_no, day-28))
    else:
        if day in range (1, 28):
            print("The immediate successor of the date is {}-{}-{}".format(yr, month_no, day+1))
        elif day == 28:
            print("The immediate successor of the day is {}-{}-0{}".format(yr, month_no+1, day-27))
        else:
            print("The year is not a leap year,enter the date in between 1 to 28")
# apply the condition for the month Dec
elif month_no == 12:
    if day in range (1, 31):
        print("The immediate successor of the date is {}-{}-{}".format(yr, month_no, day+1))
    elif day == 31:
        print("The immediate successor of the date is {}-0{}-0{}".format(yr+1, month_no-11, day-30))
    else:
        print("Enter the date in between 1 to 31")
