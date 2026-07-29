# from tkinter import *

# def miles_to_km():
#     miles = float(miles_input.get())
#     km = miles * 1.609
#     kilometer_result_label.config(text=f"{km}")
    

# window = Tk()
# window.title("Miles to kilometer Converter")
# window.config(padx=20, pady=20)

# miles_input = Entry(width=7)
# miles_input.grid(column=1, row=0)

# miles_label = Label(text="Miles")
# miles_label.grid(column=2, row=0)

# equal_to_label = Label(text="is equal to")
# equal_to_label.grid(column=0, row=1)

# kilometer_result_label = Label(text="0")
# kilometer_result_label.grid(column=1, row=1)

# kilometer_label = Label(text="Km")
# kilometer_label.grid(column=2, row=1)

# calculate_button = Button(text="Calculate", command=miles_to_km)
# calculate_button.grid(column=1, row=2)

# window.mainloop()



from tkinter import *
from tkinter import ttk
from converter import convert
from constants import *


history = []


# ------------------------
# Convert
# ------------------------

def calculate(event=None):

    try:

        value = float(value_entry.get())

        result = convert(
            value,
            from_unit.get(),
            to_unit.get()
        )

        result_label.config(
            text=f"{result:.2f}"
        )

        text = f"{value} {from_unit.get()} → {result:.2f} {to_unit.get()}"

        history.insert(0, text)

        history_box.delete(0, END)

        for item in history[:10]:
            history_box.insert(END, item)

    except:

        result_label.config(
            text="Invalid Input"
        )


# ------------------------
# Swap
# ------------------------

def swap():

    first = from_unit.get()

    second = to_unit.get()

    from_unit.set(second)

    to_unit.set(first)

    calculate()


# ------------------------
# Clear
# ------------------------

def clear():

    value_entry.delete(0, END)

    result_label.config(text="0")

    history_box.delete(0, END)

    history.clear()


# ------------------------
# Window
# ------------------------

window = Tk()

window.title(WINDOW_TITLE)

window.config(
    padx=20,
    pady=20,
    bg=BACKGROUND
)

# ------------------------
# Title
# ------------------------

Label(
    text="Unit Converter",
    font=FONT_TITLE,
    fg=TEXT_COLOR,
    bg=BACKGROUND
).grid(
    row=0,
    column=0,
    columnspan=3,
    pady=10
)

# ------------------------
# Value
# ------------------------

Label(
    text="Value",
    fg=TEXT_COLOR,
    bg=BACKGROUND
).grid(row=1, column=0)

value_entry = Entry(width=15)

value_entry.grid(row=1, column=1)

value_entry.focus()

value_entry.bind("<Return>", calculate)

# ------------------------
# From
# ------------------------

Label(
    text="From",
    fg=TEXT_COLOR,
    bg=BACKGROUND
).grid(row=2, column=0)

from_unit = StringVar()

from_unit.set("Miles")

from_menu = ttk.Combobox(

    textvariable=from_unit,

    values=[
        "Miles",
        "Kilometers",
        "Celsius",
        "Fahrenheit",
        "Kilograms",
        "Pounds",
        "Centimeters",
        "Inches"
    ],

    state="readonly"
)

from_menu.grid(row=2, column=1)

# ------------------------
# To
# ------------------------

Label(
    text="To",
    fg=TEXT_COLOR,
    bg=BACKGROUND
).grid(row=3, column=0)

to_unit = StringVar()

to_unit.set("Kilometers")

to_menu = ttk.Combobox(

    textvariable=to_unit,

    values=[
        "Miles",
        "Kilometers",
        "Celsius",
        "Fahrenheit",
        "Kilograms",
        "Pounds",
        "Centimeters",
        "Inches"
    ],

    state="readonly"
)

to_menu.grid(row=3, column=1)

# ------------------------
# Buttons
# ------------------------

Button(

    text="Convert",

    width=12,

    command=calculate

).grid(row=4, column=0, pady=15)

Button(

    text="Swap",

    width=12,

    command=swap

).grid(row=4, column=1)

Button(

    text="Clear",

    width=12,

    command=clear

).grid(row=4, column=2)

# ------------------------
# Result
# ------------------------

Label(

    text="Result",

    fg=TEXT_COLOR,

    bg=BACKGROUND,

    font=FONT_NORMAL

).grid(row=5, column=0)

result_label = Label(

    text="0",

    fg="yellow",

    bg=BACKGROUND,

    font=("Arial", 14, "bold")

)

result_label.grid(row=5, column=1)

# ------------------------
# History
# ------------------------

Label(

    text="History",

    fg=TEXT_COLOR,

    bg=BACKGROUND,

    font=FONT_NORMAL

).grid(row=6, column=0, pady=10)

history_box = Listbox(

    width=45,

    height=8

)

history_box.grid(

    row=7,

    column=0,

    columnspan=3

)

window.mainloop()