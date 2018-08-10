# import the required module
import tkinter as tk
import sys

# create the main window
root = tk.Tk()
# Give the window a title
root.title('Calculator!')
# Don't let the user to resize the window
root.resizable(0, 0)
# Create the frame geometry
root.geometry('400x250')

# Create the label and place it inside the frame
x_label = tk.Label(text = 'X')
x_label.grid(row = 0, column = 0)
y_label = tk.Label(text = 'Y')
y_label.grid(row = 1, column = 0)
label = tk.Label(text = 'Choose any operand button below to calculate')
label.grid(row = 2, columnspan = 4)

# Create the entry field for the user and place it inside the frame
x_entry = tk.Entry()
x_entry.grid(row = 0, column = 1)
y_entry = tk.Entry()
y_entry.grid(row = 1, column = 1)

# Define the functions for calculation
def add():
    result = float(x_entry.get()) + float(y_entry.get())
    calculate_answer = '{}\n'.format(result)
    text_answer.insert(tk.END, calculate_answer)

def substract():
    result = float(x_entry.get()) - float(y_entry.get())
    calculate_answer = '{}\n'.format(result)
    text_answer.insert(tk.END, calculate_answer)

def multiply():
    result = float(x_entry.get()) * float(y_entry.get())
    calculate_answer = '{}\n'.format(result)
    text_answer.insert(tk.END, calculate_answer)

def divide():
    result = float(x_entry.get()) / float(y_entry.get())
    calculate_answer = '{:.3f}\n'.format(result)
    text_answer.insert(tk.END, calculate_answer)

def quit():
    sys.exit()

# Create the button and place it inside the frame
add_button = tk.Button(text = 'Add', command = add)
add_button.grid(row = 3, column = 0)
sub_button = tk.Button(text = 'Substract', command = substract)
sub_button.grid(row = 3, column = 1)
mul_button = tk.Button(text = 'Multiply', command = multiply)
mul_button.grid(row = 3, column = 2)
div_button = tk.Button(text = 'Divide', command = divide)
div_button.grid(row = 3, column = 3)
exit_button = tk.Button(text = 'Quit', command = quit)
exit_button.grid(row = 4, column = 2)

# Create the area where the answer will be displayed and place it inside the frame
text_answer = tk.Text(master = root, width = 20, height = 7)
text_answer.grid(row = 4, column = 1)

root.mainloop()
