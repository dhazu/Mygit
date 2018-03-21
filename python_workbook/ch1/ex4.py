"""Exercise 4: Area of a Field
Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.
Hint: There are 43,560 square feet in an acre."""

#Solution:
l=float(input("Enter the length of the farmer's field(in feet):"))
w=float(input("Enter the width of the farmer's field(in feet):"))
area=l*w
area_acres = area/43560

print("The area of the field in acres is {:.2f}".format(area_acres)) 
