from tkinter import Button, Tk, Label
from button_functions import number, dot, backspace, switch_sign, clear_entry, clear, calculate, history


PADX = 3
PADY = 3
HISTORY_FONT = ("Arial", 8)
RESULT_FONT = ("Arial", 20)
ENTRY_FONT = ("Arial", 20)


class NewButton(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, width=6, height=3, **kwargs)

    def grid(self, *args, **kwargs):
        super().grid(*args, padx=PADX, pady=PADY, **kwargs)


class MyWindow(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Calculator")
        self.config(padx=PADX, pady=PADY)

        # Display Labels
        history_display_1 = Label(pady=PADY, text=history[0], font=HISTORY_FONT)
        history_display_1.grid(row=0, column=0)
        history_display_2 = Label(pady=PADY, text=history[1], font=HISTORY_FONT)
        history_display_2.grid(row=0, column=1)
        history_display_3 = Label(pady=PADY, text=history[2], font=HISTORY_FONT)
        history_display_3.grid(row=0, column=2)
        history_display_4 = Label(pady=PADY, text=history[3], font=HISTORY_FONT)
        history_display_4.grid(row=0, column=3)
        result_display = Label(pady=PADY, text=" ", font=RESULT_FONT)
        result_display.grid(row=1, column=0, columnspan=4)
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
        add_button = NewButton(text="+", command=lambda: calculate("+", number_entry, result_display, history_display_1, history_display_2, history_display_3, history_display_4))
        add_button.grid(row=4, column=3)
        subtract_button = NewButton(text="-", command=lambda: calculate("-", number_entry, result_display, history_display_1, history_display_2, history_display_3, history_display_4))
        subtract_button.grid(row=5, column=3)
        multiply_button = NewButton(text="*", command=lambda: calculate("*", number_entry, result_display, history_display_1, history_display_2, history_display_3, history_display_4))
        multiply_button.grid(row=6, column=3)
        divide_button = NewButton(text="/", command=lambda: calculate("/", number_entry, result_display, history_display_1, history_display_2, history_display_3, history_display_4))
        divide_button.grid(row=7, column=3)
        equals_button = NewButton(text="=", command=lambda: calculate("=", number_entry, result_display, history_display_1, history_display_2, history_display_3, history_display_4))
        equals_button.grid(row=7, column=2)

        # Other Buttons
        backspace_button = NewButton(text="<-", command=lambda: backspace(number_entry))
        backspace_button.grid(row=3, column=0)
        clear_entry_button = NewButton(text="CE", command=lambda: clear_entry(number_entry))
        clear_entry_button.grid(row=3, column=1)
        clear_button = NewButton(text="C", command=lambda: clear(number_entry, result_display))
        clear_button.grid(row=3, column=2)
        switch_sign_button = NewButton(text="+/-", command=lambda: switch_sign)
        switch_sign_button.grid(row=3, column=3)
        decimal_button = NewButton(text=".", command=lambda: dot(number_entry))
        decimal_button.grid(row=7, column=1)
