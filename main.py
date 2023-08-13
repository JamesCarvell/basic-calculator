from tkinter import *
from decimal import Decimal
from button_functions import number, dot, backspace, switch_sign, clear_entry, clear
from gui import NewButton, MyWindow


PADX = 3
PADY = 3
HISTORY_FONT = ("Arial", 8)
DISPLAY_FONT = ("Arial", 20)
ENTRY_FONT = ("Arial", 20)

history = ["", "", "", ""]


def calculate(operator):
    global history
    n1 = display.cget("text")
    n1_actual = n1[:-1]
    n1_sign = n1[-1]
    n2 = number_entry.cget("text")
    if n1_sign == "+":
        n3 = Decimal(n1_actual) + Decimal(n2)
    elif n1_sign == "-":
        n3 = Decimal(n1_actual) - Decimal(n2)
    elif n1_sign == "*":
        n3 = Decimal(n1_actual) * Decimal(n2)
    elif n1_sign == "/":
        n3 = Decimal(n1_actual) / Decimal(n2)
    else:
        n3 = n2
        if n1 != " ":
            history.append(n1)
            history = history[1:]
            history1.config(text=history[0])
            history2.config(text=history[1])
            history3.config(text=history[2])
            history4.config(text=history[3])
    number_entry.config(text="0")
    if operator != "=":
        display.config(text=(n3 + operator))
    else:
        display.config(text=n3)


window = MyWindow()


history1 = Label(pady=PADY, text=history[0], font=HISTORY_FONT)
history1.grid(row=0, column=0)
history2 = Label(pady=PADY, text=history[1], font=HISTORY_FONT)
history2.grid(row=0, column=1)
history3 = Label(pady=PADY, text=history[2], font=HISTORY_FONT)
history3.grid(row=0, column=2)
history4 = Label(pady=PADY, text=history[3], font=HISTORY_FONT)
history4.grid(row=0, column=3)
display = Label(pady=PADY, text=" ", font=DISPLAY_FONT)
display.grid(row=1, column=0, columnspan=4)
number_entry = Label(pady=PADY, text="0", font=ENTRY_FONT)
number_entry.grid(row=2, column=0, columnspan=4)

# Number Buttons
zero_button = NewButton(text="0", command=lambda: number("0", number_entry))
zero_button.grid(row=7, column=0)
one_button = NewButton(text="1", command=lambda: number("1", number_entry))
one_button.grid(row=6, column=0)
two_button = NewButton(text="2", command=lambda: number("2", number_entry))
two_button.grid(row=6, column=1)
three_button = NewButton(text="3", command=lambda: number("3", number_entry))
three_button.grid(row=6, column=2)
four_button = NewButton(text="4", command=lambda: number("4", number_entry))
four_button.grid(row=5, column=0)
five_button = NewButton(text="5", command=lambda: number("5", number_entry))
five_button.grid(row=5, column=1)
six_button = NewButton(text="6", command=lambda: number("6", number_entry))
six_button.grid(row=5, column=2)
seven_button = NewButton(text="7", command=lambda: number("7", number_entry))
seven_button.grid(row=4, column=0)
eight_button = NewButton(text="8", command=lambda: number("8", number_entry))
eight_button.grid(row=4, column=1)
nine_button = NewButton(text="9", command=lambda: number("9", number_entry))
nine_button.grid(row=4, column=2)

# Calculation Buttons
add_button = NewButton(text="+", command=lambda: calculate("+"))
add_button.grid(row=4, column=3)
subtract_button = NewButton(text="-", command=lambda: calculate("-"))
subtract_button.grid(row=5, column=3)
multiply_button = NewButton(text="*", command=lambda: calculate("*"))
multiply_button.grid(row=6, column=3)
divide_button = NewButton(text="/", command=lambda: calculate("/"))
divide_button.grid(row=7, column=3)
equals_button = NewButton(text="=", command=lambda: calculate("="))
equals_button.grid(row=7, column=2)

# Other Buttons
backspace_button = NewButton(text="<-", command=lambda: backspace(number_entry))
backspace_button.grid(row=3, column=0)
clear_entry_button = NewButton(text="CE", command=lambda: clear_entry(number_entry))
clear_entry_button.grid(row=3, column=1)
clear_button = NewButton(text="C", command=lambda: clear(number_entry, display))
clear_button.grid(row=3, column=2)
switch_sign_button = NewButton(text="+/-", command=lambda: switch_sign)
switch_sign_button.grid(row=3, column=3)
decimal_button = NewButton(text=".", command=lambda: dot(number_entry))
decimal_button.grid(row=7, column=1)

window.mainloop()
