"""Exercise 47: Birth Date to Astrological Sign
The horoscopes commonly reported in newspapers use the position of the sun at the
time of one’s birth to try and predict the future. This system of astrology divides the
year into twelve zodiac signs, as outline in the table below:
    Zodiac sign         Date range
    -----------         ----------
    Capricorn           December 22 to January 19
    Aquarius            January 20 to february 18
    Pisces              February 19 to March 20
    Aries               March 21 to April 19
    Taurus              April 20 to May 20
    Gemini              May 21 to June 20
    Cancer              June 21 to July 22
    Leo                 July 23 to August 22
    Virgo               August 23 to September 22
    Libra               September 23 to October 22
    Scorpio             October 23 to November 21
    Sagittarius         November 22 to December 21

    Write a program that asks the user to enter his or her month and day of birth. Then
your program should report the user’s zodiac sign as part of an appropriate output
message.
"""

## Solution:

# ask the user to enter the name, birth month and date
name = input("Enter your name: ").title()
month = input("Enter the month in which you have born(enter like jan, feb, etc...): ").title()
date = int(input("Enter the date of your birthday: "))

# apply the condition to get the correct result
if (month == 'Jan' and date in range(20, 32)) or (month == 'Feb' and date in range(1, 19)):
    print("{}, your zodiac sign is Aquarius.".format(name))
elif month == 'Feb' and date >= 19:
    # check for the leap year so that a valid date in the feb month is accepted
    answer = input("Is the year you have born is leap year(Y/N)? ").upper()
    if answer == 'Y':
        if date in range(19, 30):
            print("{}, your zodiac sign is Pisces.".format(name))
        else:
            print("Enter a valid date")
    else:
        if date in range(19, 29):
            print("{}, your zodiac sign is Pisces.".format(name))
        else:
            print("Enter a valid date")
elif month == 'Mar' and date in range(1,21):
    print("{}, your zodiac sign is Pisces.".format(name))
elif (month == 'Mar' and date in range(21, 32)) or (month == 'Apr' and date in range(1, 20)):
    print("{}, your zodiac sign is Aries.".format(name))
elif (month == 'Apr' and date in range(20, 31)) or (month == 'May' and date in range(1, 21)):
    print("{}, your zodiac sign is Taurus.".format(name))
elif (month == 'May' and date in range(21, 32)) or (month == 'Jun' and date in range(1, 21)):
    print("{}, your zodiac sign is Gemini.".format(name))
elif (month == 'Jun' and date in range(21, 31)) or (month == 'July' and date in range(1, 23)):
    print("{}, your zodiac sign is Cancer.".format(name))
elif (month == 'July' and date in range(1, 24)) or (month == 'Aug' and date in range(1, 23)):
    print("{}, your zodiac sign is Leo.".format(name))
elif (month == 'Aug' and date in range(23, 32)) or (month == 'Sep' and date in range(1, 31)):
    print("{}, your zodiac sign is Virgo.".format(name))
elif (month == 'Sep' and date in range(22, 31)) or (month == 'Oct' and date in range(1, 23)):
    print("{}, your zodiac sign is Libra.".format(name))
elif (month == 'Oct' and date in range(23, 32)) or (month == 'Nov' and date in range(1, 22)):
    print("{}, your zodiac sign is Scorpio.".format(name))
elif (month == 'Nov' and date in range(22, 31)) or (month == 'Dec' and date in range(1, 22)):
    print("{}, your zodiac sign is Sagitarius.".format(name))
elif (month == 'Dec' and date in range(22, 32)) or (month == 'Jan' and date in range(1, 20)):
    print("{}, your zodiac sign is Capricorn.".format(name))
# ensure a valid date for each month is always entered
elif month != 'Feb' and date >= 32:
    print("Enter a valid date")
