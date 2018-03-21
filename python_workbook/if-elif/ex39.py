"""Exercise 39: Sound Levels
The following table lists the sound level in decibels for several common noises.
Noice               Decibal level (dB)
-----               -----------------
jackhammer     :    130
Gas lawnmower  :    106
Alarm Clock    :    70
Quiet room     :    40
    Write a program that reads a sound level in decibels from the user. If the user
enters a decibel level that matches one of the noises in the table then your program
should display a message containing only that noise. If the user enters a number
of decibels between the noises listed then your program should display a message
indicating which noises the level is between. Ensure that your program also generates
reasonable output for a value smaller than the quietest noise in the table, and for a
value larger than the loudest noise in the table."""

##Solution:

# ask the user to enter the sound level
dB = float(input("Enter the sound level: "))

# apply the condition 
if dB >= 40 and dB <= 130:
    if dB == 40:
        print("Sound level is Quiet room")
    elif dB == 70:
        print("Sound level is Alarm Clock")
    elif dB > 40 and dB < 70:
        print("Sound level is in between Quiet room and Alarm Clock")
    elif dB == 106:
        print("Sound level is Gas lawnmower")
    elif dB > 70 and dB < 106:
        print("Sound level in between Alarm Clock and Gas lawnmower")
    elif dB == 130:
        print("Sound level is Jackhammer")
    elif dB > 106 and dB < 130:
        print("Sound level is in between Gas lawnmower and Jackhammer")
else:
    print("Out of range!..Enter a value in the range 40-130")
