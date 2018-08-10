"""Fantasy Game Inventory
You are creating a fantasy video game. The data structure to model the
player’s inventory will be a dictionary where the keys are string values
describing the item in the inventory and the value is an integer value detail-
ing how many of that item the player has. For example, the dictionary value
{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the
player has 1 rope, 6 torches, 42 gold coins, and so on.
    Write a function named displayInventory() that would take any possible
“inventory” and display it like the following:
    Inventory:
    12 arrow
    42 gold coin
    1 rope
    6 torch
    1 dagger
    Total number of items: 62"""

## Solution:
# create a dictionary
itemslist = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# assign a variable total with the value 0
total = 0

# define a function to calculate the number each item contains and also the total number
def displayInventory(listitem, item):
    global total # assign the variable total as gloabl
    value = listitem[item]
    total += value
    return value

# print the result
print("Inventory:")
print(str(displayInventory(itemslist, 'arrow')) + ' arrow')
print(str(displayInventory(itemslist, 'gold coin')) + ' gold coin')
print(str(displayInventory(itemslist, 'rope')) + ' rope')
print(str(displayInventory(itemslist, 'torch')) + ' torch')
print(str(displayInventory(itemslist, 'dagger')) + ' dagger')
print("Total number of items: {}".format(total))

