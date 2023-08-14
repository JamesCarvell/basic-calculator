from decimal import Decimal

history = ["", "", "", ""]


def number(number_text, entry_field):
    if (entry_field.cget("text") == "0") or (entry_field.cget("text") == " "):
        entry_field.config(text=number_text)
    elif (entry_field.cget("text") == "-0") or (entry_field.cget("text") == "- "):
        entry_field.config(text=("-" + number_text))
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
    else:
        entry = "-" + entry
    entry_field.config(text=entry)


def clear_entry(entry_field):
    entry_field.config(text=" ")


def clear(entry_field, display_field):
    clear_entry(entry_field)
    display_field.config(text=" ")


def calculate(operator, entry, *results):
    global history
    entry_string = entry.cget("text")
    result_string = results[0].cget("text")

    if (entry_string[-1] == " ") and (result_string == " "):
        return

    result_string_sign = result_string[-1]
    result_string_number = result_string[:-1]

    if (entry_string[-1] == " ") and (operator == "="):
        return
    elif (entry_string[-1] == " ") and result_string_sign.isdigit():
        results[0].config(text=(result_string + operator))
        return
    elif entry_string[-1] == " ":
        results[0].config(text=(result_string_number + operator))
        return

    if result_string_sign == "+":
        new_result_decimal = Decimal(result_string_number) + Decimal(entry_string)
    elif result_string_sign == "-":
        new_result_decimal = Decimal(result_string_number) - Decimal(entry_string)
    elif result_string_sign == "*":
        new_result_decimal = Decimal(result_string_number) * Decimal(entry_string)
    elif result_string_sign == "/":
        new_result_decimal = Decimal(result_string_number) / Decimal(entry_string)
    else:
        new_result_decimal = Decimal(entry_string)
        if result_string != " ":
            history.append(result_string)
            history = history[1:]
            results[1].config(text=history[0])
            results[2].config(text=history[1])
            results[3].config(text=history[2])
            results[4].config(text=history[3])
    entry.config(text=" ")
    if operator != "=":
        results[0].config(text=(str(new_result_decimal) + operator))
    else:
        results[0].config(text=(str(new_result_decimal)))
