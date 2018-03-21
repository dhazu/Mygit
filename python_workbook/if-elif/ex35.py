"""Exercise 35: Dog Years
It is commonly said that one human year is equivalent to 7 dog years. However this
simple conversion fails to recognize that dogs reach adulthood in approximately two
years. As a result, some people believe that it is better to count each of the first two
human years as 10.5 dog years, and then count each additional human year as 4 dog
years.
    Write a program that implements the conversion from human years to dog years
described in the previous paragraph. Ensure that your program works correctly for
conversions of less than two human years and for conversions of two or more human
years. Your program should display an appropriate error message if the user enters
a negative number."""

##Solution:

# ask the user to enter the number of years
human_yr = int(input("Enter the number of human years: "))

# apply the condition and display the result
if human_yr > 0:
    if human_yr >= 2:
        dog_yr = 10.5 + (human_yr-2) * 4
        print("{:.1f} yr".format(dog_yr))
    else:
        print("Enter a value greater than or equal to 2")
else:
    print("Enter a value greater than zero")
