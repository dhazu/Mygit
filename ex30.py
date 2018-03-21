"""Exercise 30: Units of Pressure
In this exercise you will create a program that reads a pressure from the user in kilo-
pascals. Once the pressure has been read your program should report the equivalent
pressure in pounds per square inch, millimeters of mercury and atmospheres. Use
your research skills to determine the conversion factors between these units."""

## Solution:

# ask the user to enter the pressure
k_p = float(input("Enter the pressure(in kilo pascals): "))

# Convert the pressure into pound per square inch
p_sqre_inch = k_p*0.1450377377

# Display the result 
print("The equivalent pressure of {:.3f} kilo pascals is {:.3f} pounds per square inch.".format(
        k_p, p_sqre_inch))
