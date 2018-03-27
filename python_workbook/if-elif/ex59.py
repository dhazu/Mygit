"""Exercise 59: Is a License Plate Valid?
In a particular jurisdiction, older license plates consist of three uppercase letters
followed by three numbers. When all of the license plates following that pattern had
been used, the format was changed to four numbers followed by three uppercase
letters.
    Write a program that begins by reading a string of characters from the user. Then
your program should display a message indicating whether the characters are valid
for an older style license plate or a newer style license plate. Your program should
display an appropriate message if the string entered by the user is not valid for either
style of license plate."""

## Solution:
# ask the user to enter a plate number
plate = input("Enter the plate number: ")

# apply the condition to get the right answer
if len(plate) == 6 and plate[0] >= "A" and plate[0] <= "Z" and\
        plate[1] >= "A" and plate[1] <= "Z" and\
        plate[2] >= "A" and plate[2] <= "Z" and\
        plate[3] >= "0" and plate[3] <= "9" and\
        plate[4] >= "0" and plate[4] <= "9" and\
        plate[5] >= "0" and plate[5] <= "9":
            print ("The plate is a valid older style number plate")
elif len(plate) == 7 and plate[0] >= "0" and plate[0] <= "9" and \
        plate[1] >= "0" and plate[1] <= "9" and \
        plate[2] >= "0" and plate[2] <= "9" and \
        plate[3] >= "0" and plate[3] <= "9" and \
        plate[4] >= "A" and plate[4] <= "Z" and \
        plate[5] >= "A" and plate[5] <= "Z" and \
        plate[6] >= "A" and plate[6] <= "Z":
            print ("The plate is a valid newer style number plate")
else:
    print ("The plate is not a valid number plate")
            
