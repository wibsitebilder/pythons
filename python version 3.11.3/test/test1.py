import tkinter as tk

# Create a new window
window = tk.Tk()

# Set the window title
window.title("Calculator")

# Set the window size
window.geometry("300x450")

# Create a text box to display the input and output
text_box = tk.Entry(window, width=40, borderwidth=5)
text_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define functions to handle button clicks
def button_click(number):
    current = text_box.get()
    text_box.delete(0, tk.END)
    text_box.insert(0, str(current) + str(number))

def button_clear():
    text_box.delete(0, tk.END)

def button_add():
    first_number = text_box.get()
    global f_num
    global math_operation
    math_operation = "addition"
    f_num = int(first_number)
    text_box.delete(0, tk.END)

def button_subtract():
    first_number = text_box.get()
    global f_num
    global math_operation
    math_operation = "subtraction"
    f_num = int(first_number)
    text_box.delete(0, tk.END)

def button_multiply():
    first_number = text_box.get()
    global f_num
    global math_operation
    math_operation = "multiplication"
    f_num = int(first_number)
    text_box.delete(0, tk.END)

def button_divide():
    first_number = text_box.get()
    global f_num
    global math_operation
    math_operation = "division"
    f_num = int(first_number)
    text_box.delete(0, tk.END)

def button_equals():
    second_number = text_box.get()
    text_box.delete(0, tk.END)

    if math_operation == "addition":
        text_box.insert(0, f_num + int(second_number))
    elif math_operation == "subtraction":
        text_box.insert(0, f_num - int(second_number))
    elif math_operation == "multiplication":
        text_box.insert(0, f_num * int(second_number))
    elif math_operation == "division":
        text_box.insert(0, f_num / int(second_number))

# Create buttons for numbers and operations
button_1 = tk.Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=40, pady=20, command=lambda:button_click(4))
button_5 = tk.Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_clear = tk.Button(window, text="Clear", padx=79, pady=20, command=button_clear)
button_add = tk.Button(window, text="+", padx=39, pady=20, command=button_add)
button_subtract = tk.Button(window, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = tk.Button(window, text="*", padx=40, pady=20, command=button_multiply)
button_divide = tk.Button(window, text="/", padx=41, pady=20, command=button_divide)

button_equals = tk.Button(window,text="=", padx=91, pady=20, command=button_equals)

# Place the buttons on the window using the grid layout manager
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_equals.grid(row=5, column=1, columnspan=2)

# Start the main event loop
window.mainloop()