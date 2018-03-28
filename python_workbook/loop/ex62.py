# -*- coding:utf-8 -*-
"""Exercise 62: Discount Table
(18 Lines)
A particular retailer is having a 60 percent off sale on a variety of discontinued
products. The retailer would like to help its customers determine the reduced price
of the merchandise by having a printed discount table on the shelf that shows the
original prices and the prices after the discount has been applied. Write a program that
uses a loop to generate this table, showing the original price, the discount amount,
and the new price for purchases of $4.95, $9.95, $14.95, $19.95 and $24.95. Ensure
that the discount amounts and the new prices are rounded to 2 decimal places when
they are displayed."""

## Solution:

# creat a list containing the price tag
price_tag = [4.95, 9.95, 14.95, 19.95, 24.95]

# use for loop to loop through each value of the list
for i in range(len(price_tag)):
    original_price = price_tag[i]    
    discount_amount = price_tag[i] * 0.6  # calculate the discount amonut
    new_price = original_price - discount_amount  # calculate the price after the discount

    # Display the result
    print("original_price  = ${:>5.2f}".format(original_price))
    print("discount_amount = ${:>5.2f}".format( discount_amount))
    print("new_price       = ${:>5.2f}".format(new_price))
    # Print a doted line after each value               
    print('-' * 30)
