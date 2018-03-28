"""Exercise 63: Temperature Conversion Table
Write a program that displays a temperature conversion table for degrees Celsius and
degrees Fahrenheit. The table should include rows for all temperatures between 0
and 100 degrees Celsius that are multiples of 10 degrees Celsius. Include appropriate
headings on your columns. The formula for converting between degrees Celsius and
degrees Fahrenheit can be found on the internet."""

## Solution:

#Define a function to convert degree celcius to fahrenheit
def degC_F():
    print("Degree Celcius to Fahrenheit")
    for i in range(1, 100):           # temperature in between 0 to 100
        if i % 10 == 0:               # accept the temperatures those are multiples of 10
            temp_F = (i * 9/5) + 32   # convert the temperature to fahrenheit
            # display the result
            print("""                 
            temp(deg C)   temp(deg F)
            ----------    ----------
            {}            {:>6.2f}""" .format(i, temp_F))     

# Define a function to convert fahrenheit to degree celcius            
def degF_C():
    print("Fahenheit to degree celcius")
    for i in range(1, 100):
        if i % 10 == 0: 
            temp_C = (i - 32) * 5/9   # convert the temperature to degree celcius
            # display the result
            print("""
            temp(deg F)   temp(deg C)
            -----------   -----------
            {}            {:>6.2f}""".format(i, temp_C))

# ask the user to whether they want to do the convertion
answer = input("Now we are going to convert the temperature to fahrenheit. Do you want(Y/N)? ").upper()
if answer == 'Y':
    # calling the function
    degC_F()
else:
    pass

answer2 = input("Do you want to convert the temperature to degree celcius(Y/N)? ").upper()
if answer2 == 'Y':
    # calling the function
    degF_C()
else: 
    pass

