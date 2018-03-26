# -*- coding: utf-8 -*-
"""Exercise 55: Frequency to Name
(31 Lines)
Electromagnetic radiation can be classified into one of 7 categories according to its
frequency, as shown in the table below:

    Name                Frequency range (Hz)
    ----                --------------------
    Radio waves         Less than 3 × 10^9
    Microwaves          3 × 10^9 to less than 3 × 10^12
    Infrared light      3 × 10^12 to less than 4.3 × 10^14
    Visible light       4.3 × 10^14 to less than 7.5 × 10^14
    Ultraviolet light   7.5 × 10^14 to less than 3 × 10^17
    X-rays              3 × 10^17 to less than 3 × 10^19
    Gamma rays          3 × 10^19 or more

    Write a program that reads the frequency of the radiation from the user and displays
the appropriate name."""

# Solution:
from math import pow

def freq_name():
    freq = float(raw_input("Enter the frequency of the raditaion(in Hz): "))
    global name
    if freq < 3*pow(10,9):
        name = 'Radio waves'
    elif 3*pow(10,9) <= freq < 3*pow(10, 12):
        name = 'Microwaves'
    elif 3*pow(10,12) <= freq < 4.3*pow(10, 14):
        name = 'Infrared light'
    elif 4.3*pow(10, 14) <= freq < 7.5*pow(10, 14):
        name = 'Visible light'
    elif 7.5*pow(10, 14) <= freq < 3*pow(10, 17):
        name = 'Ultraviolet light'
    elif 3*pow(10, 17) <= freq < 3*pow(10, 19):
        name = 'X-rays'
    elif freq >= 3*pow(10, 19):
        name = 'Gamma rays'
    else:
        name = ""

freq_name()
print "The name of the frequency is %s" % name
