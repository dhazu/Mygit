"""Exercise 28: Wind Chill
When the wind blows in cold weather, the air feels even colder than it actually is
because the movement of the air increases the rate of cooling for warm objects, like
people. This effect is known as wind chill.
    In 2001, Canada, the United Kingdom and the United States adopted the fol-
lowing formula for computing the wind chill index. Within the formula Ta is the
air temperature in degrees Celsius and V is the wind speed in kilometers per hour.
A similar formula with different constant values can be used with temperatures in
degrees Fahrenheit and wind speeds in miles per hour."""
#  WCI = 13.12 + 0.6215Ta − 11.37V^0.16 + 0.3965TaV^0.16
"""Write a program that begins by reading the air temperature and wind speed from the
user. Once these values have been read your program should display the wind chill
index rounded to the closest integer."""
#The wind chill index is only considered valid for temperatures less than or
#equal to 10 degrees Celsius and wind speeds exceeding 4.8 kilometers per
#hour.

## SOLUTION:
WC_OFFSET = 13.12
WC_FACTOR1 = 0.625
WC_FACTOR2 =  -11.37
WC_FACTOR3 = 0.3965
WC_EXPONENT = 0.16

# ask the user to enter the speed of the wind and temperature of the air
V = float(input("Enter the speed of the wind(in kilometer per hour)(>=4.8 Kms/hr): "))
Ta = float(input("Enter the temperature of the air(in degree celsius)(<=10 deg cel): "))

# Now compute the WCI
WCI = WC_OFFSET+WC_FACTOR1*Ta+WC_FACTOR2*(V**WC_EXPONENT)+WC_FACTOR3*Ta*(V**WC_EXPONENT)

# Display the result
print("The wind chill index is {:f}".format(WCI))

