"""Write a function named printTable() that takes a list of lists of strings
and displays it in a well-organized table with each column right-justified.
Assume that all the inner lists will contain the same number of strings.
For example, the value could look like this:
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'moose', 'goose']]

Your printTable() function would print the following:
    apples Alice  dogs
   oranges   Bob  cats
  cherries Carol moose
    banana David goose
"""
## Solution:
tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):   # Define the function
    length = 0          # create a variable to length to store the length of the largest value of in the lists 
                        # and initially assigned a value 0 to it.
    for lists in data:  # find the largest string in the lists
        for word in lists:
            if len(word) > length:
                length = len(word)
    for i in range(4):  # create the loop
        for j in range(len(data)):
            print(data[j][i].rjust(length), end='')
        print()

printTable(tableData)
