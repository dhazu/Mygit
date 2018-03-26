"""Exercise 56: Cell Phone Bill
A particular cell phone plan includes 50 minutes of air time and 50 text messages
for $15.00 a month. Each additional minute of air time costs $0.25, while additional
text messages cost $0.15 each. All cell phone bills include an additional charge of
$0.44 to support 911 call centers, and the entire bill (including the 911 charge) is
subject to 5 percent sales tax.
    Write a program that reads the number of minutes and text messages used in a
month from the user. Display the base charge, additional minutes charge (if any),
additional text message charge (if any), the 911 fee, tax and total bill amount. Only
display the additional minute and text message charges if the user incurred costs in
these categories. Ensure that all of the charges are displayed using 2 decimal places."""

## Solution:

# ask the user to enter the talk time and number of text message
minutes = int(input("Enter the number of minutes of air time: "))
text = int(input("Enter the number of text messgae send: "))

# charge of the 911 call center 
fee_911 = 0.44

# apply the condition and calculate the base_price, tax and total_bil
if minutes <= 50 and text <= 50:
    base_price = 15   # base price is $15.00
    tax = (base_price + fee_911) * 0.05   # tax is 5 percent
    total_bil = base_price + fee_911 + tax
else:
    if minutes > 50 and text <= 50:
        diff1 = minutes - 50
        base_price = 15 + diff1 * 0.25    # each additional air time will costs $0.25
        tax = (base_price + fee_911) * 0.05
        total_bil = base_price + fee_911 + tax
    elif text > 50 and minutes <= 50:
        diff2 = text - 50 
        base_price = 15 + diff2 * 0.15   # each additional text messages will costs $0.15
        tax = (base_price + fee_911) * 0.05
        total_bil = base_price + fee_911 + tax
    elif minutes > 50 and text > 50:
        diff1 = minutes - 50
        diff2 = text - 50
        base_price = 15 + diff1 * 0.25 + diff2 * 0.15
        tax = (base_price + fee_911) * 0.05
        total_bil = base_price + fee_911 + tax

# Display the result
print("Base price is            = ${:.2f}".format(base_price))
if minutes > 50 and text <= 50:
    print("Additional minutes   = {}".format(diff1))
elif text > 50 and minutes <= 50:
    print("Additional text msg  = {}".format(diff2))
elif minutes > 50 and text > 50:
    print("Additional miutes    = {}".format(diff1))
    print("Additional text msg  = {}".format(diff2))
else:
    pass

print("911 fee is               = ${:.2f}".format(fee_911))
print("tax amount is            = ${:.2f}".format(tax))
print("Total amount is          = ${:.2f}".format(total_bil))

    
