"""Exercise 17: Heat Capacity
The amount of energy required to increase the temperature of one gram of a material
by one degree Celsius is the material’s specific heat capacity, C. The total amount
of energy required to raise m grams of a material by ΔT degrees Celsius can be
computed using the formula:
q = mCΔT.
    Write a program that reads the mass of some water and the temperature change
from the user. Your program should display the total amount of energy that must be
added or removed to achieve the desired temperature change."""
#Hint: The specific heat capacity of water is (4.186)J/g◦C . Because water has a den-
#sity of 1.0 gram per millilitre, you can use grams and millilitres interchangeably
#in this exercise. 	
"""Extend your program so that it also computes the cost of heating the water. Elec-
tricity is normally billed using units of kilowatt hours rather than Joules. In this
exercise, you should assume that electricity costs 8.9 cents per kilowatt-hour. Use
your program to compute the cost of boiling water for a cup of coffee."""
#Hint: You will need to look up the factor for converting between Joules and
#kilowatt hours to complete the last part of this exercise.

## Solution:

# ask the user to enter the required inputs
m = float(input("Enter the mass of the water(in millitre): "))
T1 = float(input("Enter the intial temperature of the water(in deg celcius): ")) 
T2 = float(input("Enter the present temperature of the water(in deg celcius): "))

# apply the condition so that the temperature difference always positive
if T1>T2:
    dT = T1-T2
else:
    dT = T2-T1
C = 4.186

# calculate the result of the first part of the problem
q = m*C*dT

# Display the result of the first part of the problem
print("""
The amount of energy required to change the {:.2f} deg cel temperature of {:.2f} millitre of water
is {:.3f} J""".format(dT, m, q)) 
print()
# Calculate the result of the second part of the problem
J_TO_KHW=2.777e-7
electricty_cost=8.9
KWH=q*J_TO_KHW
cost=KWH*8.9

# Display the result
print("The cost of the electricity will be {:.3f} cents".format(cost))


