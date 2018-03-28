"""Exercise 6: Tax and Tip
The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places."""

#Solution:

price = float(input("Enter the price of the meal(in rupees): "))
tip = price * 0.18
tax = float(input("Enter the amount of tax (in percent): "))
tax_meal = price * tax/100
cost = price + tip + tax_meal
print() 
print("The price of the meal is      = {:>10.2f} rupees".format(price))
print("The tip for the meal is       = {:>10.2f} rupees".format(tip))
print("The tax on the meal is        = {:>10.2f} rupees".format(tax_meal))
print("-" * 50)
print("The total cost of the meal is = {:>10.2f} rupees".format(cost)) 
