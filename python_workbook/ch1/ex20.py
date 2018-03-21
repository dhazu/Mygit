"""Exercise 20: Ideal Gas Law
The ideal gas law is a mathematical approximation of the behavior of gasses as
pressure, volume and temperature change. It is usually stated as:
PV = nRT
    where P is the pressure in Pascals, V is the volume in liters, n is the amount of
substance in moles, R is the ideal gas constant, equal to 8.314 J/mol*K , and T is the
temperature in degrees Kelvin.
    Write a program that computes the amount of gas in moles when the user supplies
the pressure, volume and temperature. Test your program by determining the number
of moles of gas in a SCUBA tank. A typical SCUBA tank holds 12 liters of gas at
a pressure of 20,000,000 Pascals (approximately 3,000 PSI). Room temperature is
approximately 20 degrees Celsius or 68 degrees Fahrenheit."""

#Hint: A temperature is converted from Celsius to Kelvin by adding 273.15
#to it. To convert a temperature from Fahrenheit to Kelvin, deduct 32 from it,
#multiply it by 59 and then add 273.15 to it.

## Solution:
# ask the user to enter the required inputs
P = float(input("Enter the amount of pressure of the gas tank (in pascals): "))
V = float(input("Enter the volume of the tank (in litre): "))
T = float(input("Enter the temperature of the tank(in deg celcius): "))

# convert the temperature to degree Kelvin
T_K = T+273.15

R = 8.314  # R is the ideal gas constant

# calculate the number of moles
n = (P*V)/(R*T)

# Display the result
print("The amount of gas moles in the tank is {}".format(n))

# Calculate the number of moles of gas in the SCUBA tank
V_SCUBA = 12 
P_SCUBA = 20000000
T_SCUBA = 20
T_SCUBA_K = 20+273.15
R = 8.314
n_SCUBA = (P_SCUBA*V_SCUBA)/(R*T_SCUBA)

# Display the result
print("""
The amount of moles in the SCUBA tank having {} ltrs gas at a pressure
of {} Pascals and temperature {} deg celsius is {}""".format(
V_SCUBA, P_SCUBA, T_SCUBA, n_SCUBA))
