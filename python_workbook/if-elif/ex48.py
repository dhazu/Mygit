"""Exercise 48: Chinese Zodiac
The Chinese zodiac assigns animals to years in a 12 year cycle. One 12 year cycle is
shown in the table below. The pattern repeats from there, with 2012 being another
year of the dragon, and 1999 being another year of the hare.
Year                Animal
----                ------
2000                Dragon
2001                Snake
2002                Horse
2003                Sheep
2004                Monkey
2005                Rooster
2006                Dog
2007                Pig
2008                Rat
2009                Ox
2010                Tiger
2011                Hare
    Write a program that reads a year from the user and displays the animal associated
with that year. Your program should work correctly for any year greater than or equal
to zero, not just the ones listed in the table."""

## Solution:

# ask the user to enter a year
year = int(input("Enter the year: "))

if year <= 0:   # ensure a positive value is always entered
    print("Enter a valid year.")

# apply the condition to get the correct answer
else:
    if year % 12 == 8:
        print("The animal associated with this year is Dragon.")
    elif year % 12 == 9:
        print("The animal associated with this year is Snake.")
    elif year % 12 == 10:
        print("The animal assocaited with this year is Horse.")
    elif year % 12 == 11:
        print("The animal associated with this year is Sheep.")
    elif year % 12 == 0:
        print("The animal associated with this year is Monkey.")
    elif year % 12 == 1:
        print("The animal associated with this year is Rooster.")
    elif year % 12 == 2:
        print("The animal associated with this year is Dog.")
    elif year % 12 == 3:
        print("The animal assocaited with this year is Pig.")
    elif year % 12 == 4:
        print("The animal associate with this year is Rat.")
    elif year % 12 == 5:
        print("The animal associated with this year is Ox.")
    elif year % 12 == 6:
        print("The animal associated with this year is Tiger.")
    elif year % 12 == 7:
        print("The year associated with this year is Hare.")
