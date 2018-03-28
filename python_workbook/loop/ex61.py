"""Exercise 61: Average
In this exercise you will create a program that computes the average of a collection
of values entered by the user. The user will enter 0 as a sentinel value to indicate
that no further values will be provided. Your program should display an appropriate
error message if the first value entered by the user is 0.
    #Hint: Because the 0 marks the end of the input it should not be included in the average.
"""
## Solution:
# intialised the variables
add = 0
avg = 0
count = 0

# creat an empty list to store the numbers entered by the user
collection = []

# ask the user to enter how many numbers to be entered
num = int(input("Enter how many numbers to be entered: "))

# Ensure that the user will enter atleast one number
if num > 0:
    # Now apply the for loop to calculate the result
    for i in range(num):
        x = int(input("Enter num{} number: ".format(i)))  # prompt the user to enter the numbers
        # Warn the user not to enter zero as first number        
        if i == 0 and x == 0:   
            print("Don't enter 'zero' as first value")
            break     # zero is act as sentinel value and the program will stopped
        elif x == 0:  # while user enter zero as number
            break     # as well as the user enters 0 as number the loop will stopped
        else:
            collection.append(x)  # insert the numbers to the lists
            count += 1
            add += collection[i]  # add the numbers

        # calculate the average
        avg = add / float(count)

    # display the result
    if i == 0 and x == 0:
        pass
    else:
        print("avg = {:.2f}".format(avg))
else:
    print("Need atleast one number to calculate the average")
