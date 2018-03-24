"""Exercise 53: Assessing Employees
At a particular company, employees are rated at the end of each year. The rating scale
begins at 0.0, with higher values indicating better performance and resulting in larger
raises. The value awarded to an employee is either 0.0, 0.4, or 0.6 or more. Values
between 0.0 and 0.4, and between 0.4 and 0.6 are never used. The meaning associated
with each rating is shown in the following table. The amount of an employee’s raise
is $2400.00 multiplied by their rating.

    Rating                  meaning
    ------                  -------
    0.0                     Unacceptable performance
    0.4                     Acceptable performance
    0.6 or more             Meritorious performance

     Write a program that reads a rating from the user and indicates whether the perfor-
mance was unacceptable, acceptable or meritorious. The amount of the employee’s
raise should also be reported. Your program should display an appropriate error
message if an invalid rating is entered."""

# Solution:
# convert the performance meaning to a letter code
c = 'Unacceptable performance'
b = 'Acceptable performance'
a = 'Meritorious performance'

# ask the user to enter a rating scale
rating_value = float(input("Enter the rating scale of the employee(usually a floating value): "))

if rating_value == 0.0:
    rating = c
    amount = 0     # amount is multiplied by their rating value
elif rating_value == 0.4:
    rating = b
    amount = rating_value * 2400
elif rating_value >= 0.6:
    rating = a
    amount = rating_value * 2400
else:
    rating = 'invalid'

# Display the result
if rating == 'invalid':
    print("Enter a valid rating value.")
else:
    print("""
The performance of the employee was {} and the rasise in amount is {:.2f}""".format(
        rating, amount))

