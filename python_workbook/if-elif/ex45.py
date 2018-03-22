"""Exercise 45: What Color is that Square?
Positions on a chess board are identified by a letter and a number. The letter identifies
the column, while the number identifies the row:    
    Write a program that reads a position from the user. Use an if statement to deter-
mine if the column begins with a black square or a white square. Then use modular
arithmetic to report the color of the square in that row. For example, if the user enters
a1 then your program should report that the square is black. If the user enters d5
then your program should report that the square is white. Your program may assume
that a valid position will always be entered. It does not need to perform any error
checking."""

## Solution:

# ask the user to enter the position of the chess board
pos = input("Enter the position of the chess board(e.g a1,b6,g4..etc):").lower()

# now abstract the alphabetice part and the numeric part of the position and assign it to separate variable
alpha = pos[0]
num = int(pos[1])

# Now apply the condition and display the result
if alpha == 'a' or alpha == 'c' or alpha == 'e' or alpha == 'g':
    if num in range(1, 8, 2):
        print("The square is black.")
    elif num in range(2, 9, 2):
        print("The square is white.")
    else:
        print("Enter a row number from 1 to 8")
elif alpha == 'b' or alpha == 'd' or alpha == 'f' or alpha == 'h':
    if num in range(1, 8, 2):
        print("The square is white.")
    elif num in range(2, 9, 2):
        print("The square is black.")
    else:
        print("Enter a row number from 1 to 8")
else:
    print("Enter a position between 'a1' to 'h8'.")
