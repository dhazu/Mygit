"""Regex Search
Write a program that opens all .txt files in a folder and searches for any
line that matches a user-supplied regular expression. The results should
be printed to the screen."""

## Solution
# import the required module
import os
import re

# create a regex object
myregex = re.compile(r'\w+\s+\w+\s')

# create an empty list to hold the text file from the directory
mylist = []

# search all files in the directory and then separte the .txt file and place it 
# inside the list
for filename in os.listdir('.'):
    if filename.endswith('.txt'):
        mylist += [filename]

# open the every file in mylist and then read it and then
# search for every match pattern created in the content of the every file
# and then print it separated by a comma
for filename in mylist:
    text = open(filename)
    x = text.read()
    for word in myregex.findall(x):
        print(word, end =',')
    print('\n')
