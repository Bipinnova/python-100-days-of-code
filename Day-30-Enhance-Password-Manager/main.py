from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
# def find_password():
#     website = website_entry.get()
#     try:
#         with open("data.json") as data_file:
#             data = json.load(data_file)
#     except FileNotFoundError:
#         messagebox.showinfo(title="Error", message="No Data File Found.")
#     else:
#         if website in data:
#             email = data[website]["email"]
#             password = data[website]["password"]
#             messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
#         else:
#             messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

def find_password():
    website = website_entry.get().strip().lower()

    # Check empty field
    if not website:
        messagebox.showwarning(
            title="Missing Website",
            message="Please enter a website name to search."
        )
        website_entry.focus()
        return

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(
            title="File Not Found",
            message="No saved password database was found."
        )

    except json.JSONDecodeError:
        messagebox.showerror(
            title="Invalid Data",
            message="The password database is empty or corrupted."
        )

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]

            # Copy password automatically
            pyperclip.copy(password)

            messagebox.showinfo(
                title="Password Found",
                message=(
                    f"🌐 Website : {website}\n\n"
                    f"📧 Email    : {email}\n"
                    f"🔑 Password : {password}\n\n"
                    "✅ Password has been copied to your clipboard."
                )
            )

        else:
            messagebox.showinfo(
                title="Not Found",
                message=f"No saved account found for '{website}'."
            )

    website_entry.focus()


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
    width=22,
    font=FONT,
    relief="solid",
    bg=ENTRY_BG
)
website_entry.grid(row=2, column=1, padx=5)
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

# Search
search_button = Button(
    text="🔍 Search",
    width=10,
    font=("Segoe UI", 10, "bold"),
    bg="#24292F",
    fg="white",
    activebackground="#1B1F23",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    bd=0,
    padx=10,
    pady=5,
    command=find_password
)

search_button.grid(row=2, column=2, padx=(5, 0))
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

