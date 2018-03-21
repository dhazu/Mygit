"""Exercise 27: Body Mass Index
    Write a program that computes the body mass index (BMI) of an individual. Your
program should begin by reading a height and weight from the user. Then it should
use one of the following two formulas to compute the BMI before displaying it. If
you read the height in inches and the weight in pounds then body mass index is
computed using the following formula:"""
#    BMI = (weight*703)/(height*height)
"""If you read the height in meters and the weight in kilograms then body mass index
is computed using this slightly simpler formula:"""
#    BMI = weight/(height*height)

## Solution:
# ask the user to choose the choice
print("Would you like to enter height and weight in inches and pound or meters and kgs?")
print("If you like inches and pound then type 'Y',else type 'N'")
choice = input("? ").upper()
if  choice == 'Y':
    # ask the user to enter the height and weight 
    h = float(input("Enter the height of the body(in inches): "))
    w = float(input("Enter the weight of the body(in pounds): "))
    
    # calculate the BMI
    BMI = (w*703)/(h*h)

    # Display the result
    print("The BMI of the body is {:.3f}".format(BMI))

else:
    # ask the user to enter the height and weight
    h = float(input("Enter the height of the body (in meters): "))
    w = float(input("Enter the weight of the body (in kgs): "))
    
    # Calculate the BMI
    BMI = w/(h*h)

    # Display the result
    print("The BMI of the body is {:.3f}".format(BMI))
