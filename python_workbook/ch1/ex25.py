"""Exercise 25: Units of Time (Again)
In this exercise you will reverse the process described in the previous exercise.
    Develop a program that begins by reading a number of seconds from the user.
Then your program should display the equivalent amount of time in the form
D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and sec-
onds respectively. The hours, minutes and seconds should all be formatted so that
they occupy exactly two digits, with a leading 0 displayed if necessary."""

## Solution:
# ask the user to enter the number of second
S = int(input("Enter how many seconds: "))

# Now calculte the number of days from the given number of seconds
D = S // (3600*24) 

# Now extract the remainder after calculating the number of days
S = S % (3600*24)

# Display the number of days followed by a colon
print("{}".format(D),':', sep='', end='')

# Now calculte the number of hours from the remaining seconds
H = S//3600

# Now calculate the remaining time after the division
S = S % 3600

# Now calculate the tens and ones digit of hours so that it will occupy exactly two digits
tens = H // 10
ones = H % 10

# Display the number of hours
print("{}{}".format(tens,ones),':',sep='',end='')

# Now calculate the number of minutes from the remaining time
M = S // 60

# Now calculate the reminder after the division
S = S % 60

# Now calculate the tens and ones digit of minutes
tens = M // 10
ones = M % 10

# Display the number of minutes
print("{}{}".format(tens,ones),':',sep='',end='')

# Now calculate the tens and ones digit of the remaining time
tens = S // 10
ones = S % 10

# Display the tens and ones digit of the remaining seconds
print("{}{}".format(tens,ones))
