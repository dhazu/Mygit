"""Exercise 29: Celsius to Fahrenheit and Kelvin
Write a program that begins by reading a temperature from the user in degrees
Celsius. Then your program should display the equivalent temperature in degrees
Fahrenheit and degrees Kelvin. The calculations needed to convert between different
units of temperature can be found on the internet."""

##Solution:

# ask the user to enter the temperature
temp_cel = float(input("Enter the temperature in degree celsius:"))

# Now convert the temperature into degree fahrenheit
temp_fah = (9/5)*temp_cel+32

# Now convert the temperature into degree kelvin
temp_kel = temp_cel+273.15

print("""
The equivalent temp of {:.2f} deg celsius in deg fahrenheit is {:.2f} and 
in deg kelvin is {:.2f}""".format(temp_cel, temp_fah, temp_kel))
