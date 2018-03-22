"""Exercise 43: Faces on Money
It is common for images of a country’s previous leaders, or other individuals of his-
torical significance, to appear on its money. The individuals that appear on banknotes
in the United States are listed in Table 2.1.
    Write a program that begins by reading the denomination of a banknote from the
user. Then your program should display the name of the individual that appears on the
banknote of the entered amount. An appropriate error message should be displayed
if no such note exists."""
"""
Table 2.1 Individuals that appear on Banknotes
Individual                  Amount
----------                  ------
George Washington           $1
Thomas Jefferson            $2
Abraham Lincoln             $5
Alexander Hamilton          $10
Andrew Jackson              $20
Ulysses S. Grant            $50
Benjamin Franklin           $100
"""
"""While two dollar banknotes are rarely seen in circulation in the United States,
they are legal tender that can be spent just like any other denomination. The
United States has also issued banknotes in denominations of $500, $1,000,
$5,000, and $10,000 for public use. However, high denomination banknotes
have not been printed since 1945 and were officially discontinued in 1969. As
a result, we will not consider them in this exercise."""

##Solution:

# ask the user to enter amonut of the banknote
amount = float(input("Enter the amount of the banknote(in $): "))

# apply the condition to get the required result
if amount == 1:
    name = 'George Washington'
elif amount == 2:
    name = 'Thomas Jefferson'
elif amount == 5:
    name = 'Abraham Lincoln'
elif amount == 10:
    name = 'Alexander Hamiltion'
elif amount == 20:
    name = 'Andrew Jackson'
elif amount == 50:
    name = 'Ulysses S. Grant'
elif amount == 100:
    name = 'Benjamin Franklin'
elif amount == 500 or amount == 1000 or amount == 5000 or amount == 10000:
    name = 'discontinued'
else:
    name = ''

# Now display the result
if name == '':
    print("These banknotes are not in the list")
elif name == 'discontinued':
    print("These banknotes are officially discontinued")
else:
    print("The indivisual on the banknote is {}".format(name))
