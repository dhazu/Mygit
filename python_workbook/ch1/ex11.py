"""Exercise 11: Fuel Efficiency
In the United States, fuel efficiency for vehicles is normally expressed in miles-per-
gallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
kilometers (L/100 km). Use your research skills to determine how to convert from
MPG to L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units."""

#Solution:
MPG = float(input("Enter the fuel efficiency in American units(MPG): "))

# Convert MPG to LPH
LPH = 235.215 / MPG

# Display the result
print("The equivalent fuel efficiency of {:.2f} MPG is {:.2f} L/100km".format(MPG, LPH))
