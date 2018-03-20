"""Exercise 13: Making Change
Consider the software that runs on a self-checkout machine. One task that it must be
able to perform is to determine how much change to provide when the shopper pays
for a purchase with cash.
    Write a program that begins by reading a number of cents from the user as an
integer. Then your program should compute and display the denominations of the
coins that should be used to give that amount of change to the shopper. The change
should be given using as few coins as possible. Assume that the machine is loaded
with pennies, nickels, dimes, quarters, loonies and toonies."""
#A one dollar coin was introduced in Canada in 1987. It is referred to as a
#loonie because one side of the coin has a loon (a type of bird) on it. The two
#dollar coin, referred to as a toonie, was introduced 9 years later. It’s name is
#derived from the combination of the number two and the name of the loonie. 

## Solution:

cents_toonie = 200
cents_loonie = 100
cents_quarters = 25
cents_dimes = 10
cents_nickel = 5

# ask the user to input the number of cents
cents = int(input("Enter the number of cents: "))

# converts the cents into toonies, loonies, quarters, dimes, nickels and pennies
toonies = cents // cents_toonie
cents = cents % cents_toonie  # '%' operator used to find the reminder
loonies = cents // cents_loonie
cents = cents % cents_loonie
quarters = cents // cents_quarters
cents = cents % cents_quarters
dimes = cents // cents_dimes
cents = cents % cents_dimes
nickels = cents // cents_nickel
cents = cents % cents_nickel
pennies = cents

# Display the result
print(" ",toonies,"toonies")
print(" ",loonies,"loonies")
print(" ",quarters,"quarters")
print(" ",dimes,"dimes")
print(" ",nickels,"nickels")
print(" ",pennies,"pennies")

