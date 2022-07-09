from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters = [choice(letters) for char in range(randint(8, 10))]
    symbols = [choice(symbols) for sym in range(randint(2, 4))]
    numbers = [choice(numbers) for num in range(randint(2, 4))]

    password_list = letters + symbols + numbers
    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = entry_website.get()
    email_get = entry_email.get()
    password_get = entry_password.get()
    new_data = {
        web: {
            "email": email_get,
            "password": password_get
        }
    }

    if len(web) == 0 or len(email_get) == 0 or len(password_get) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)


def search():
    websites = entry_website.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Oops", message="No Data file found")
    else:
        if websites in data:
            messagebox.showinfo(title=websites, message=f"Email: {data[websites]['email']} \n\n"
                                                        f"Password: {data[websites]['password']}")
        else:
            messagebox.showwarning(title="Oops", message=f"No details for the {websites} exists")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img_bg = PhotoImage(file="logo.png")
canvas.create_image(130, 100, image=img_bg)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)

entry_website = Entry(width=33)
entry_website.grid(row=1, column=1, sticky=W)
entry_website.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

entry_email = Entry(width=52)
entry_email.grid(row=2, column=1, columnspan=3, sticky=W)
entry_email.insert(0, "nevero.anton@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

entry_password = Entry(width=33)
entry_password.grid(row=3, column=1, sticky=W)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=W)

search_button = Button(text="Search", width=14, command=search)
search_button.grid(row=1, column=2, columnspan=2)

window.mainloop()
