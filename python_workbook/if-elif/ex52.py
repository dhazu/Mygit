"""Exercise 52: Grade Points to Letter Grade
In the previous exercise you created a program that converts a letter grade into the
equivalent number of grade points. In this exercise you will create a program that
reverses the process and converts from a grade point value entered by the user to a
letter grade. Ensure that your program handles grade point values that fall between
letter grades. These should be rounded to the closest letter grade. Your program
should report A+ for a 4.0 (or greater) grade point average.

Letter          Grade Points
------          ------------
A+              4.0
A               4.0
A−              3.7
B+              3.3
B               3.0
B−              2.7
C+              2.3
C               2.0
C−              1.7
D+              1.3
D               1.0
F               0
"""

## Solution:
gp = float(input("Enter the grade point value: "))

# Now convert the number grade point to a letter grade point
if 4.0 < gp < 10:
    gd = 'A+'
elif gp == 4.0:
    gd = 'A'
elif 3.7 <= gp < 4.0:
    gd = 'A-'
elif 3.3 <= gp < 3.7:
    gd = 'B+'
elif 3.0 <= gp < 3.3:
    gd = 'B'
elif 2.7 <= gp < 3.0:
    gd = 'B-'
elif 2.3 <= gp < 2.7:
    gd = 'C+'
elif 2.0 <= gp < 2.3:
    gd = 'C'
elif 1.7 <= gp < 2.0:
    gd = 'C-'
elif 1.3 <= gp < 1.7:
    gd = 'D+'
elif 1.0 <= gp < 1.3:
    gd = 'D'
elif 0 <= gp < 1.0:
    gd = 'F'
else:
    gd = 0

# Display the result
if gd == 0:
    print("Enter a valid grade point")
else:
    print("The grade is {}".format(gd))
