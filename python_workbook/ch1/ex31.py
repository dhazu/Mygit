"""Exercise 31: Sum of the Digits in an Integer
Develop a program that reads a four-digit integer from the user and displays the sum
of the digits in the number. For example, if the user enters 3141 then your program
should display 3 + 1 + 4 + 1 = 9."""

## Solution:

# ask the user to enter a number
num = int(input("Enter a four digit integer number: "))

# now extract every digit of the number and then add it
digit_4 = num // 1000  # extracting the fourth digit of the number
num %=  1000           # num = num % 1000
digit_3 = num // 100   # extracting the third digit of the number
num %= 100
digit_2 = num // 10    # extracting the second digit of the number
num %= 10              # reminder will be the first place digit of the number

# Calculate the sum
sum = digit_4+digit_3+digit_2+num

# Display the sum
print("The sum of the digits of the number is {}".format(sum))
