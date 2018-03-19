"""Exercise 5: Bottle Deposits
In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
    Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places."""

#Solution:

small_container = int(input("Enter the number of drink container holding one liter or less: "))
large_container = int(input("Enter the number of drink container holding more than one liter: "))
# Calculte the result
amount = small_container * 0.10 + large_container * 0.25
# Display the result
print("The amount received will be ${:.2f}".format(amount))
 
