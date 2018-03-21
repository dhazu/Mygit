"""Exercise 36: Vowel or Consonant
In this exercise you will create a program that reads a letter of the alphabet from the
user. If the user enters a, e, i, o or u then your program should display a message
indicating that the entered letter is a vowel. If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and sometimes y is
a consonant. Otherwise your program should display a message indicating that the
letter is a consonant."""

## Solution:

# ask the user to enter a letter 
letter = input("Enter a letter :").upper()   # upper() function will convert the letter to uppercase

# apply the condition and display the result
if letter == 'A':
    print("{} is vowel".format(letter))
else:
    if letter == 'E':
        print("{} is vowel".format(letter))
    else:
        if letter == 'I':
            print("{} is vowel".format(letter)) 
        else:
            if letter == 'O':
                print("{} is vowel".format(letter))
            else:
                if letter == 'U':
                    print("{} is vowel".format(letter))
                else:
                    if letter == 'Y':
                        print("Sometimes {} is vowel or sometimes consonant".format(letter))
                    else:
                        print("{} is consonant".format(letter))

