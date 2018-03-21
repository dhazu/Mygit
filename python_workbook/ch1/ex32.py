"""Exercise 32: Sort 3 Integers
Create a program that reads three integers from the user and displays them in sorted
order (from smallest to largest). Use the min and max functions to find the smallest
and largest values. The middle value can be found by computing the sum of all three
values, and then subtracting the minimum value and the maximum value."""

## Solution:

# ask the user to enter the numbers
x = int(input("Enter the first interger number: "))
y = int(input("Enter the second integer number: "))
z = int(input("Enter the third integer number: "))

# extracting the min, mid and max number
mx = max(x,y,z)
mn = min(x,y,z)
mid = (x+y+z)-mn-mx

# Display the result
print("The numbers in the sorted order are: ")
print("{}".format(mn))
print("{}".format(mid))
print("{}".format(mx))
