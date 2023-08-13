from tkinter import Button, Tk

PADX = 3
PADY = 3


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
