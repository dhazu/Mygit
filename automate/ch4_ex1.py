"""Comma Code
Say you have a list value like this:
spam = ['apples', 'bananas', 'tofu', 'cats']
    Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and
inserted before the last item. For example, passing the previous spam list to
the function would return 'apples, bananas, tofu, and cats' . But your func-
tion should be able to work with any list value passed to it."""

# Solution:
def vic(listvalue):         # Define a function
    newvalue = ', '.join(listvalue[:len(listvalue) - 1]) + ' and ' + listvalue[-1] # add commas between each items before the second 
                                                                               # last item and add and before the last item
    return newvalue         # return the newvalue                         

spam = ['apples', 'bananas', 'tofu', 'cats', 'lucky', 'mango']    # create a list and assign it to a variable
x = vic(spam)               # call the function with spam as a parameter and returned value assign to a new variable x
print(x)                   # print the result

