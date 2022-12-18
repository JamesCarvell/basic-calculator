from tkinter import *
from decimal import *

PADX = 3
PADY = 3
HISTORY_FONT = ("Arial", 8)
DISPLAY_FONT = ("Arial", 10)
ENTRY_FONT = ("Arial", 20)
NUM_STRINGS = "0123456789"

history = ["", "", "", ""]


def number(number_text):
    number_text = number_text
    if number_entry.cget("text") == "0":
        number_entry.config(text=number_text)
    else:
        new_text = number_entry.cget("text") + number_text
        number_entry.config(text=new_text)


def zero():
    number(NUM_STRINGS[0])
def one():
    number(NUM_STRINGS[1])
def two():
    number(NUM_STRINGS[2])
def three():
    number(NUM_STRINGS[3])
def four():
    number(NUM_STRINGS[4])
def five():
    number(NUM_STRINGS[5])
def six():
    number(NUM_STRINGS[6])
def seven():
    number(NUM_STRINGS[7])
def eight():
    number(NUM_STRINGS[8])
def nine():
    number(NUM_STRINGS[9])


def dot():
    if "." not in number_entry.cget("text"):
        new_text = number_entry.cget("text") + "."
        number_entry.config(text=new_text)


def calculate():
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
    return str(n3)


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


def backspace():
    entry = number_entry.cget("text")
    if -10 < int(entry) < 10:
        entry = "0"
    else:
        entry = entry[:-1]
    number_entry.config(text=entry)


def switch_sign():
    entry = number_entry.cget("text")
    if entry[0] == "-":
        entry = entry[1:]
    elif entry == "0":
        pass
    else:
        entry = "-" + entry
    number_entry.config(text=entry)


def clear_entry():
    number_entry.config(text="0")


def clear():
    clear_entry()
    display.config(text=" ")


class NewButton(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, width=6, height=3, **kwargs)

    def grid(self, *args, **kwargs):
        super().grid(*args, padx=PADX, pady=PADY, **kwargs)


window = Tk()
window.title("Calculator")
window.config(padx=PADX, pady=PADY)

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
zero_button = NewButton(text=NUM_STRINGS[0], command=zero)
zero_button.grid(row=7, column=0)
one_button = NewButton(text=NUM_STRINGS[1], command=one)
one_button.grid(row=6, column=0)
two_button = NewButton(text=NUM_STRINGS[2], command=two)
two_button.grid(row=6, column=1)
three_button = NewButton(text=NUM_STRINGS[3], command=three)
three_button.grid(row=6, column=2)
four_button = NewButton(text=NUM_STRINGS[4], command=four)
four_button.grid(row=5, column=0)
five_button = NewButton(text=NUM_STRINGS[5], command=five)
five_button.grid(row=5, column=1)
six_button = NewButton(text=NUM_STRINGS[6], command=six)
six_button.grid(row=5, column=2)
seven_button = NewButton(text=NUM_STRINGS[7], command=seven)
seven_button.grid(row=4, column=0)
eight_button = NewButton(text=NUM_STRINGS[8], command=eight)
eight_button.grid(row=4, column=1)
nine_button = NewButton(text=NUM_STRINGS[9], command=nine)
nine_button.grid(row=4, column=2)

# Calculation Buttons
add_button = NewButton(text="+", command=add)
add_button.grid(row=4, column=3)
subtract_button = NewButton(text="-", command=subtract)
subtract_button.grid(row=5, column=3)
multiply_button = NewButton(text="*", command=multiply)
multiply_button.grid(row=6, column=3)
divide_button = NewButton(text="/", command=divide)
divide_button.grid(row=7, column=3)
equals_button = NewButton(text="=", command=equals)
equals_button.grid(row=7, column=2)

# Other Buttons
backspace_button = NewButton(text="<-", command=backspace)
backspace_button.grid(row=3, column=0)
clear_entry_button = NewButton(text="CE", command=clear_entry)
clear_entry_button.grid(row=3, column=1)
clear_button = NewButton(text="C", command=clear)
clear_button.grid(row=3, column=2)
switch_sign_button = NewButton(text="+/-", command=switch_sign)
switch_sign_button.grid(row=3, column=3)
decimal_button = NewButton(text=".", command=dot)
decimal_button.grid(row=7, column=1)

window.mainloop()

# TODO: move gui code to separate file
# TODO: move function code to separate file
# TODO: once-over to make more DRY where possible
