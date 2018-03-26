"""Exercise 50: Roots of a Quadratic Function  mkkkkkkkk.;;;;;;;;;;;
A univariate quadratic function has the form f (x) = ax^2 + bx + c, where a, b and
c are constants, and a is non-zero. The roots of a quadratic function can be found
by finding the values of x that satisfy the quadratic equation ax^2 + bx + c = 0. A
quadratic function may have 0, 1 or 2 real roots. These roots can be computed using
the quadratic formula, shown below:
    
    root = ((-b)+-square root(b^2-4ac))/2a

The portion of the expression under the square root sign is called the discriminant.
If the discriminant is negative then the quadratic equation does not have any real roots.
If the discriminant is 0, then the equation has one real root. Otherwise the equation
has two real roots, and the expression must be evaluated twice, once using a plus
sign, and once using a minus sign, when computing the numerator.
    Write a program that computes the real roots of a quadratic function. Your program
should begin by prompting the user for the values of a, b and c. Then it should display
a message indicating the number of real roots, along with the values of the real roots
(if any)."""

## Solution:

# ask the user to enter required value
a = int(input("Enter the value of a(non-zero): "))
# ensure that the user will always enter non-zero value of a 
if a != 0:
    # If user will enter a non-zero value of a then prompt for the value of b and c
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))
   
    # calculate the discriminant
    discriminant = b * b - 4 * a * c

    # apply the condition to get the correct result
    if discriminant == 0:
        print("The equation has one real root.")
    elif discriminant < 0:
        print("The equation does not have any real roots.")
    else:
        print("The equation has two real roots.")
else:
    print("Enter non-zero value of a")
