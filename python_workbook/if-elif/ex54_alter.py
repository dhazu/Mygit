"""Exercise 54: Wavelengths of Visible Light
The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the
spectrum is continuous, it is often divided into 6 colors as shown below:

    Color               Wavelength (nm) 
    -----               ---------------
    Violet              380 to less than 450
    Blue                450 to less than 495
    Green               495 to less than 570   
    Yellow              570 to less than 590
    Orange              590 to less than 620
    Red                 620 to 750

    Write a program that reads a wavelength from the user and reports its color. Display
an appropriate error message if the wavelength entered by the user is outside of the
visible spectrum."""

## Solution:

# ask the user to enter the wavelength of the light
w_len = float(input("Enter the wavelength of the light: "))

# Ensure that the user will always entered a wavelength from visible spectrum
if w_len < 380:
    print("The wavelength entered is too low to the visible spectrum")
elif w_len > 750:
    print("The wavelength entered is too high to the visible spectrum")
else:
    if 380 <= w_len < 450:  # w_len >= 380 or w_len < 450
        print("The colour of the light is Violet")
    elif 450 <= w_len < 495:
        print("The color of the light is Blue")
    elif 495 <= w_len < 570:
        print("The color of the light is Green")
    elif 570 <= w_len < 590:
        print("The color of the light is Yellow")
    elif 590 <= w_len < 620:
        print("The color of the light is Orange")
    elif 620 <= w_len <= 750:
        print("The color of the light is Red")
