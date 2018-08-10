"""Write a function named collatz() that has one parameter named number . If
number is even, then collatz() should print number // 2 and return this value.
If number is odd, then collatz() should print and return 3 * number + 1 .
Then write a program that lets the user type in an integer and that keeps
calling collatz() on that number until the function returns the value 1 ."""
## Solution:
def collatz(number):    # Define the function
    global x            # Define a global variable x
    if number % 2 == 0: # check whether the number entered is even or odd
        print("{} // 2".format(number)) 
        x = number // 2 # store the result into the varibale x
        return x        # return the value of x
    else:
        print("3 * {} + 1".format(number))
        x = 3 * number + 1
        return x

num = int(input("Enter a positive integer number: "))   # ask the user to enter a integer number

if num > 0:
    collatz(num)    # call the fuction
    print(x)        # print the value of x
    while x != 1:   # creat a loop to continue upto the value return by the function is 1
        collatz(x)
        print(x)
else:
    print("Enter a number bigger than zero")
    
