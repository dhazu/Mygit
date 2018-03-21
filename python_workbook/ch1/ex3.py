"""Exercise 3: Area of a Room
Write a program that asks the user to enter the width and length of a room. Once
the values have been read, your program should compute and display the area of the
room. The length and the width will be entered as floating point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with."""
#Solution:
w=float(input("Enter the width of the room(in feet):"))
l=float(input("Enter the length of the room(in feet):"))
area=w*l
print("The area of the room is {:.2f} sqr feet".format(area))

