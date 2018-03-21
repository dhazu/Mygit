"""Exercise 34: Even or Odd?
Write a program that reads an integer from the user. Then your program should
display a message indicating whether the integer is even or odd."""

##Solution:

# ask the user to enter a number
num = int(input("Enter an integer number: "))

# apply the condition and display the result
if num <= 0:
    print("Enter a number greater than zero")
elif num%2 == 0:      
    print("{} is even".format(num))
else:
    print("{} is odd".format(num))
