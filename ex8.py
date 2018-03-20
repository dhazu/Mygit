"""Exercise 8: Widgets and Gizmos
An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order."""

#Solution:
wid = int(input("Enter the number of widgets ordered: "))
giz = int(input("Enter the number of gizmo ordered: "))

# Calculte the total weight of the products
w_wid = wid * 75
w_giz = giz * 112
total_weight = w_wid + w_giz

# Display the result
print("The total weight ordered are {} grams".format(total_weight))
