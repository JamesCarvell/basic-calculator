from tkinter import *
from decimal import *

BUTTON_PADX = 3
BUTTON_PADY = 3
num_strings = "0123456789"


def number(number_text):
    number_text = number_text
    if number_entry.cget("text") == "0":
        number_entry.config(text=number_text)
    else:
        new_text = number_entry.cget("text") + number_text
        number_entry.config(text=new_text)


def zero():
    number(num_strings[0])
def one():
    number(num_strings[1])
def two():
    number(num_strings[2])
def three():
    number(num_strings[3])
def four():
    number(num_strings[4])
def five():
    number(num_strings[5])
def six():
    number(num_strings[6])
def seven():
    number(num_strings[7])
def eight():
    number(num_strings[8])
def nine():
    number(num_strings[9])


def dot():
    if "." not in number_entry.cget("text"):
        new_text = number_entry.cget("text") + "."
        number_entry.config(text=new_text)


def calculate():
    n1 = display.cget("text")
    n2 = number_entry.cget("text")
    if n1 == "" or n1.isdigit():
        n3 = n2
    else:
        sign = n1[-1]
        n1_actual = n1[:-1]
        if "+" in sign:
            n3 = Decimal(n1_actual) + Decimal(n2)
        if "-" in sign:
            n3 = Decimal(n1_actual) - Decimal(n2)
        if "*" in sign:
            n3 = Decimal(n1_actual) * Decimal(n2)
        if "/" in sign:
            n3 = Decimal(n1_actual) / Decimal(n2)
        n3 = str(n3)
    number_entry.config(text="0")
    return n3


def add():
    n3 = calculate()
    display.config(text=(n3 + "+"))
def subtract():
    n3 = calculate()
    display.config(text=(n3 + "-"))
def multiply():
    n3 = calculate()
    display.config(text=(n3 + "*"))
def divide():
    n3 = calculate()
    display.config(text=(n3 + "/"))
def equals():
    n3 = calculate()
    display.config(text=n3)


window = Tk()
window.title("Calculator")
window.config(padx=BUTTON_PADX, pady=BUTTON_PADY)

history1 = Label(pady=BUTTON_PADY, text="History", font=("Arial", 8))
history1.grid(row=0, column=0)
history2 = Label(pady=BUTTON_PADY, text="History", font=("Arial", 8))
history2.grid(row=0, column=1)
history3 = Label(pady=BUTTON_PADY, text="History", font=("Arial", 8))
history3.grid(row=0, column=2)
history4 = Label(pady=BUTTON_PADY, text="History", font=("Arial", 8))
history4.grid(row=0, column=3)
display = Label(pady=BUTTON_PADY, text="", font=("Arial", 10))
display.grid(row=1, column=0, columnspan=4)
number_entry = Label(pady=BUTTON_PADY, text="0", font=("Arial", 15))
number_entry.grid(row=2, column=0, columnspan=4)

# Number Buttons
zero_button = Button(text=num_strings[0], width=5, height=3, command=zero)
zero_button.grid(row=7, column=0, padx=BUTTON_PADX, pady=BUTTON_PADY)
one_button = Button(text=num_strings[1], width=5, height=3, command=one)
one_button.grid(row=6, column=0, padx=BUTTON_PADX, pady=BUTTON_PADY)
two_button = Button(text=num_strings[2], width=5, height=3, command=two)
two_button.grid(row=6, column=1, padx=BUTTON_PADX, pady=BUTTON_PADY)
three_button = Button(text=num_strings[3], width=5, height=3, command=three)
three_button.grid(row=6, column=2, padx=BUTTON_PADX, pady=BUTTON_PADY)
four_button = Button(text=num_strings[4], width=5, height=3, command=four)
four_button.grid(row=5, column=0, padx=BUTTON_PADX, pady=BUTTON_PADY)
five_button = Button(text=num_strings[5], width=5, height=3, command=five)
five_button.grid(row=5, column=1, padx=BUTTON_PADX, pady=BUTTON_PADY)
six_button = Button(text=num_strings[6], width=5, height=3, command=six)
six_button.grid(row=5, column=2, padx=BUTTON_PADX, pady=BUTTON_PADY)
seven_button = Button(text=num_strings[7], width=5, height=3, command=seven)
seven_button.grid(row=4, column=0, padx=BUTTON_PADX, pady=BUTTON_PADY)
eight_button = Button(text=num_strings[8], width=5, height=3, command=eight)
eight_button.grid(row=4, column=1, padx=BUTTON_PADX, pady=BUTTON_PADY)
nine_button = Button(text=num_strings[9], width=5, height=3, command=nine)
nine_button.grid(row=4, column=2, padx=BUTTON_PADX, pady=BUTTON_PADY)

# Calculation Buttons
add_button = Button(text="+", width=5, height=3, command=add)
add_button.grid(row=4, column=3, padx=BUTTON_PADX, pady=BUTTON_PADY)
subtract_button = Button(text="-", width=5, height=3, command=subtract)
subtract_button.grid(row=5, column=3, padx=BUTTON_PADX, pady=BUTTON_PADY)
multiply_button = Button(text="*", width=5, height=3, command=multiply)
multiply_button.grid(row=6, column=3, padx=BUTTON_PADX, pady=BUTTON_PADY)
divide_button = Button(text="/", width=5, height=3, command=divide)
divide_button.grid(row=7, column=3, padx=BUTTON_PADX, pady=BUTTON_PADY)
equals_button = Button(text="=", width=5, height=3, command=equals)
equals_button.grid(row=7, column=2, padx=BUTTON_PADX, pady=BUTTON_PADY)

# Other Buttons
decimal_button = Button(text=".", width=5, height=3, command=dot)
decimal_button.grid(row=7, column=1, padx=BUTTON_PADX, pady=BUTTON_PADY)
backspace_button = Button(text="<-", width=5, height=3)
backspace_button.grid(row=3, column=0, padx=BUTTON_PADX, pady=BUTTON_PADY)
clear_entry_button = Button(text="CE", width=5, height=3)
clear_entry_button.grid(row=3, column=1, padx=BUTTON_PADX, pady=BUTTON_PADY)
clear_button = Button(text="C", width=5, height=3)
clear_button.grid(row=3, column=2, padx=BUTTON_PADX, pady=BUTTON_PADY)
switch_sign_button = Button(text="+/-", width=5, height=3)
switch_sign_button.grid(row=3, column=3, padx=BUTTON_PADX, pady=BUTTON_PADY)

window.mainloop()

# TODO: equals function
# TODO: history label updates
# TODO: clear function
# TODO: clear entry function
# TODO: backspace function
# TODO: switch sign function
# TODO: move gui code to separate file
# TODO: move function code to separate file
# TODO: once-over to make more DRY where possible
