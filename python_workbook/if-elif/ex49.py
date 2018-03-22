"""Exercise 49: Richter Scale
The following table contains earthquake magnitude ranges on the Richter scale and
their descriptors:
    
    Magnitude                           Descriptor
    ---------                           ---------
    Less than 2.0                       Micro
    2.0 to less than 3.0                Very Minor
    3.0 to less than 4.0                Minor
    4.0 to less than 5.0                Light
    5.0 to less than 6.0                Moderate
    6.0 to less than 7.0                Strong
    7.0 to less than 8.0                Major
    8.0 to less than 10.0               Great
    10.0 or more                        Meteoric

    Write a program that reads a magnitude from the user and displays the appropriate
descriptor as part of a meaningful message. For example, if the user enters 5.5 then
your program should indicate that a magnitude 5.5 earthquake is considered to be a
moderate earthquake."""

##Solution:

# ask the user to enter the magnitude of the earthquake
mag = float(input("Enter the magnitude of the earthquake: "))

# apply the condition to get the correct answer
if mag < 2.0:
    print("The earthquake is considered to be a micro earthquake.")
elif 2.0 <= mag < 3.0:
    print("The earthquake is considered to be a Very Minor earthquake.")
elif 3.0 <= mag < 4.0:
    print("The earthquake is considered to be a Minor earthquake.")
elif 4.0 <= mag < 5.0:
    print("The earthquake is considered to be a Light earthquake.")
elif 5.0 <= mag < 6.0:
    print("The earthquake is considered to be a Moderate earthquake.")
elif 6.0 <= mag < 7.0:
    print("The earthquake is considered to be a Strong earthquake.")
elif 7.0 <= mag < 8.0:
    print("The earthquake is considered to be a Major earthquake.")
elif 8.0 <= mag < 10.0:
    print("The earthquake is considered to be a Great earthquake.")
elif mag >= 10.0:
    print("The earthquake is considered to be a Meteoric earthquake.")
