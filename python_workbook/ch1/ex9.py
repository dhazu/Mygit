"""Exercise 9: Compound Interest
Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places."""

#Solution:
P = float(input("Enter the amount of money deposited (in rupees): "))
r = 0.04
n = 12
t = 1

# Compute the amonut after each year
A1 = P * (1+r/n) ** (n*t)
A2 = A1 * (1+r/n) ** (n*t)
A3 = A2 * (1+r/n) ** (n*t)

# Display the amount
print("The amount in the savings after the first year is {:.2f} rupees".format(A1))

print("The amount in the savings after the second year is {:.2f} rupees".format(A2)) 

print("The amount in the savings after the third year is {:.2f} rupees".format(A3)) 
