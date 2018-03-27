"""Exercise 60: Roulette Payouts
A roulette wheel has 38 spaces on it. Of these spaces, 18 are black, 18 are red, and two
are green. The green spaces are numbered 0 and 00. The red spaces are numbered 1,
3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 and 36. The remaining integers
between 1 and 36 are used to number the black spaces.
Many different bets can be placed in roulette. We will only consider the following
subset of them in this exercise:
    •   Single number (1 to 36, 0, or 00)
    •   Red versus Black
    •   Odd versus Even (Note that 0 and 00 do not pay out for even)
    •   1 to 18 versus 19 to 36
        Write a program that simulates a spin of a roulette wheel by using Python’s random
    number generator. Display the number that was selected and all of the bets that must
    be payed. For example, if 13 is selected then your program should display:

    The spin resulted in 13..
    Pay 13
    Pay Black
    Pay Odd
    Pay 1 to 18
        If the simulation results in 0 or 00 then your program should display Pay 0 or
    Pay 00 without any further output."""

## Solution:
# import randrange module from random module
from random import randrange

# Simulate spining the wheel, using 37 to represent 00
num = randrange(0,38) 
if num == 37:
    print ("The spin resulted in 00....")
else:
    print ("The spin resulted in {}...".format(num))

# Display the payout for a single number
if num == 37:
    print ("pay 00")
else:
    print ("pay", num)

#Display the colour payout
#The first line in the condition checks for 1,3,5,7,9
#The second line in the condition checks for 12,14,16,18
#The third line in the condition checks for 19,21,23,25,27
#The fouth line in the condition checks for 30,32,34,36

if num in range(1,10,2) or \
        num in range(12,19,2) or \
        num in range(19, 28,2) or \
        num in range(30,37,2):
            print ("Black")
elif num == 0 or num == 37:
    pass
else:
    print ("Red")

#Display the odd vs even
if num in range(1, 37):
    if num % 2 == 1:
        print ("Odd")
    else:
        print ("Even")

# Display the lower number vs. upper number payout
if num in range(1, 19):
    print ("Pay 1 to 18")
elif num in range(19, 37):
    print ("Pay 19 to 36")


