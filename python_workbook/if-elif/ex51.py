"""Exercise 51: Letter Grade to Grade Points
At a particular university, letter grades are mapped to grade points in the following
manner:
    Letter              Grade points
    ------              ------------
    A+                  4.0
    A                   4.0
    A−                  3.7
    B+                  3.3
    B                   3.0
    B−                  2.7
    C+                  2.3
    C                   2.0
    C−                  1.7
    D+                  1.3
    D                   1.0
    F                   0
    
    Write a program that begins by reading a letter grade from the user. Then your
program should compute and display the equivalent number of grade points. Ensure
that your program generates an appropriate error message if the user enters an invalid
letter grade.
"""

## solution:
# Covert the letter grade point to a number of grade point
A = 4.0
A_MINUS = 3.7
B_PLUS = 3.3
B = 3.0
B_MINUS = 2.7
C_PLUS = 2.3
C = 2.0
C_MINUS = 1.7
D_PLUS = 1.3
D = 1.0
F = 0
INVALID = -1

# ask the user to enter the letter grade
grade = input("Enter the letter grade of the grade chart(like A, A+, B- etc): ").upper()

# Now apply the condition to convert the letter grade to a number of grade point 
if grade == "A+" or grade == "A":
     gp = A
elif grade == "A-":
     gp = A_MIUNS
elif grade == "B+":
     gp = B_PLUS
elif grade == "B":
     gp = B
elif grade == "B-":
     gp = B_MINUS
elif grade == "C+":
     gp = C_PLUS
elif grade == "C":
     gp = C
elif grade == "C-":
     gp = C_MINUS
elif grade == "D+":
     gp = D_PLUS
elif grade == "D":
     gp = D
elif grade == "F":
     gp = F 
else:
     gp = INVALID
    
# Now display the result
if gp == INVALID:
    print("That wasn't a valid grade point letter.")
else:
    print("The equivalent Grade point is {}".format(gp))

