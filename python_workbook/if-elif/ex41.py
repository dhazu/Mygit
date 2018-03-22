"""Exercise 41: Note To Frequency
The following table lists an octave of music notes, beginning with middle C, along
with their frequencies.
note                frequency(Hz)
----                -------------
C4                  261.63
D4                  293.66
E4                  329.63
F4                  349.23
G4                  392.00
A4                  440.00
B4                  493.88
    Begin by writing a program that reads the name of a note from the user and
displays the note’s frequency. Your program should support all of the notes listed
previously.
    Once you have your program working correctly for the notes listed previously you
should add support for all of the notes from C0 to C8. While this could be done by
adding many additional cases to your if statement, such a solution is cumbersome,
inelegant and unacceptable for the purposes of this exercise. Instead, you should
exploit the relationship between notes in adjacent octaves. In particular, the frequency
of any note in octave n is half the frequency of the corresponding note in octave n +1.
By using this relationship, you should be able to add support for the additional notes
without adding additional cases to your if statement."""
#Hint:
"""To complete this exercise you will need to extract individual characters
from the two-character note name so that you can work with the letter and
the octave number separately. Once you have separated the parts, compute the
frequency of the note in the fourth octave using the data in the table above.
Then divide the frequency by 2^4−x , where x is the octave number entered by
the user. This will halve or double the frequency the correct number of times."""

##Solution:

# Convert the name of the notes to its frequency
C4_Freq = 261.63
D4_Freq = 293.66
E4_Freq = 329.63
F4_Freq = 349.23
G4_Freq = 392.00
A4_Freq = 440.00
B4_Freq = 493.88

# Read the note from the user
name = input("Enter the two character name note, such as C4: ").upper()

# Store the notes and its octaves in separate variable
note = name[0]
octave = int(name[1])

#Get the frequency of the note, assuming it is in the fourth octave
if octave == 4:
    if note  == 'C':
        freq = C4_Freq
    elif note == 'D':
        freq = D4_Freq
    elif note == 'E':
        freq = E4_Freq
    elif note == 'F':
        freq = F4_Freq
    elif note == 'G':
        freq = G4_Freq
    elif note == 'A':
        freq = A4_Freq
    elif note == 'B':
        freq = B4_Freq

    #Now adjust the frequency to bring it into the correct octave
    freq = freq / 2 ** (4 - octave)

    #Display the result
    print("The frequency of {} is {:.2f}".format(name, freq))
else:
    print("Enter a valid note name.")
