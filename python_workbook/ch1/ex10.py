# - *- coding: utf- 8 - *-
"""Exercise 10: Arithmetic
Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
. The quotient when a is divided by b
. The remainder when a is divided by b
. The result of log 10 a
. The result of a to be power b """

## Solution:
# importing log and pow functions from math module
from math import log10, pow

# Ask the user to enter the number
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Do the calculations
sum = a + b
dif = a - b
pro = a * b
quo = a / b
rem = a % b
log = log10(a)
pow = int(pow(a,b))

# Display the result
print("The sum is {}".format(sum))
print("The difference is {}".format(dif))
print("The product is {}".format(pro))
print("The quotient is {:.3f}".format(quo))
print("The reminder is {}".format(rem))
print("The result of log10{} is {}".format(a, log))
print("The result of {} to be power {} is {}".format(a, b, pow))
