def number(number_text, entry_field):
    if entry_field.cget("text") == "0":
        entry_field.config(text=number_text)
    else:
        new_text = entry_field.cget("text") + number_text
        entry_field.config(text=new_text)


def dot(entry_field):
    if "." not in entry_field.cget("text"):
        new_text = entry_field.cget("text") + "."
        entry_field.config(text=new_text)


def backspace(entry_field):
    entry = entry_field.cget("text")
    if -10 < int(entry) < 10:
        entry = "0"
    else:
        entry = entry[:-1]
    entry_field.config(text=entry)


def switch_sign(entry_field):
    entry = entry_field.cget("text")
    if entry[0] == "-":
        entry = entry[1:]
    elif entry == "0":
        pass
    else:
        entry = "-" + entry
    entry_field.config(text=entry)


def clear_entry(entry_field):
    entry_field.config(text="0")


def clear(entry_field, display_field):
    clear_entry(entry_field)
    display_field.config(text=" ")
