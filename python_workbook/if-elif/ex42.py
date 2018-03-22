"""Exercise 42: Frequency To Note
In the previous question you converted from note name to frequency. In this question
you will write a program that reverses that process. Begin by reading a frequency
from the user. If the frequency is within one Hertz of a value listed in the table in
the previous question then report the name of the note. Otherwise report that the
frequency does not correspond to a known note. In this exercise you only need to
consider the notes listed in the table. There is no need to consider notes from other
octaves."""

## Solution:

# ask the user to enter the frequency of the note and display the note (if any) that is corresponds to
C4_FREQ = 261.63
D4_FREQ = 293.66
E4_FREQ = 329.63
F4_FREQ = 349.23
G4_FREQ = 392.00
A4_FREQ = 440.00
B4_FREQ = 493.88

freq = float(input("Enter the frequency of a note(in Hz): "))

# apply the condition and display the corrent value
if freq == C4_FREQ:
    print("The name of the note is C4.")
elif freq == D4_FREQ:
    print("The name of the note is D4.")
elif freq == E4_FREQ:
    print("The name of the note is E4.")
elif freq == F4_FREQ:
    print("The name of the note is F4.")
elif freq == G4_FREQ:
    print("The name of the note is G4.")
elif freq == A4_FREQ:
    print("The name of the note is A4.")
elif freq == B4_FREQ:
    print("The name of the note is B4.")
else:
    print("The frequency does not correspond to a known note.")
   
    
