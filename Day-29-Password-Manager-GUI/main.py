from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip # type: ignore

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password)

    messagebox.showinfo(
        title="Password Generated",
        message="A strong password has been generated and copied to your clipboard."
    )


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if website == "" or password == "":
        messagebox.showerror(
            title="Missing Information",
            message="Website and Password fields cannot be empty."
        )
        return

    if "@" not in email or "." not in email:
        messagebox.showerror(
            title="Invalid Email",
            message="Please enter a valid email address."
        )
        return

    is_ok = messagebox.askokcancel(
        title="Confirm Details",
        message=f"""Please confirm the following details:

Website : {website}
Email    : {email}
Password : {password}

Do you want to save this password?
"""
    )

    if is_ok:
        with open("data.txt", "a", encoding="utf-8") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")

        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()

        messagebox.showinfo(
            title="Success",
            message="Password saved successfully!"
        )




# ---------------------------- COLORS ------------------------------- #
BG_COLOR = "#F4F6F9"
ENTRY_BG = "#FFFFFF"
BTN_COLOR = "#4CAF50"
BTN_TEXT = "#FFFFFF"
FONT = ("Segoe UI", 11)
TITLE_FONT = ("Segoe UI", 20, "bold")

# ---------------------------- WINDOW ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=30, bg=BG_COLOR)
window.resizable(False, False)

# ---------------------------- TITLE ------------------------------- #
title = Label(
    text="🔐 Password Manager",
    font=TITLE_FONT,
    bg=BG_COLOR,
    fg="#2C3E50"
)
title.grid(row=0, column=0, columnspan=3, pady=(0, 20))

# ---------------------------- LOGO ------------------------------- #
canvas = Canvas(
    width=200,
    height=200,
    bg=BG_COLOR,
    highlightthickness=0
)

logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=1, column=0, columnspan=3, pady=(0, 20))

# ---------------------------- LABELS ------------------------------- #

website_label = Label(
    text="Website",
    font=FONT,
    bg=BG_COLOR
)
website_label.grid(row=2, column=0, sticky="e", pady=8)

email_label = Label(
    text="Email / Username",
    font=FONT,
    bg=BG_COLOR
)
email_label.grid(row=3, column=0, sticky="e", pady=8)

password_label = Label(
    text="Password",
    font=FONT,
    bg=BG_COLOR
)
password_label.grid(row=4, column=0, sticky="e", pady=8)

# ---------------------------- ENTRIES ------------------------------- #

website_entry = Entry(
    width=38,
    font=FONT,
    relief="solid",
    bg=ENTRY_BG
)
website_entry.grid(row=2, column=1, columnspan=2, padx=5)
website_entry.focus()

email_entry = Entry(
    width=38,
    font=FONT,
    relief="solid",
    bg=ENTRY_BG
)
email_entry.grid(row=3, column=1, columnspan=2, padx=5)
email_entry.insert(0, "your_email@example.com")

password_entry = Entry(
    width=22,
    font=FONT,
    relief="solid",
    bg=ENTRY_BG
)
password_entry.grid(row=4, column=1, padx=5)

# ---------------------------- BUTTONS ------------------------------- #

generate_password_button = Button(
    text="Generate",
    font=("Segoe UI", 10, "bold"),
    bg=BTN_COLOR,
    fg=BTN_TEXT,
    activebackground="#43A047",
    activeforeground="white",
    relief="flat",
    padx=10,
    command=generate_password
)
generate_password_button.grid(row=4, column=2, padx=5)

add_button = Button(
    text="Add Password",
    width=35,
    font=("Segoe UI", 10, "bold"),
    bg="#2196F3",
    fg="white",
    activebackground="#1976D2",
    activeforeground="white",
    relief="flat",
    pady=5,
    command=save
)
add_button.grid(row=5, column=1, columnspan=2, pady=20)

# ---------------------------- MAIN LOOP ------------------------------- #

window.mainloop()

