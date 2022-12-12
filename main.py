from tkinter import *
from tkinter import messagebox
from os.path import exists
from random import choice, shuffle, randint
import pyperclip

messagebox.showinfo(message="WELCOME TO KEYCELLAR.")
# PASSWORD GENERATOR
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list = [choice(letters) for char in range(randint(8, 10))]

    password_list += [choice(symbols) for char in range(randint(2, 4))]

    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(message="PASSWORD COPIED.")

# SAVE PASSWORD
def store_pass():
    site = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(site) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=site, message=f"These are the details entered:\n \nEmail: {email}\nPassword: {password}\n\nIs it ok to save?")

        if is_ok:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            if not exists("data.txt"):
                with open("data.txt", "a") as pass_data:
                    pass_data.write(" ----- SITE || EMAIL || PASSWORD -----\n\n")

            with open("data.txt", "a") as pass_data:
                pass_data.write(f"\t{site} || {email} || {password}\n")
# UI SETUP
window = Tk()
window.title("KEYCELLAR")
window.config(padx=50, pady=50)
logo_canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
logo_canvas.create_image(100, 100, image=logo_img)
logo_canvas.grid(row=0, column=1)

# Left-side descriptive labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
login_label = Label(text="Email/Username:")
login_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

# Entry boxes for user inputs
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

email_entry.insert(0, "@gmail.com")

password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)

# Buttons to store and generate password
gen_pass_btn = Button(text="Generate Password", command=gen_pass)
gen_pass_btn.grid(row=3, column=2)

store_pass_btn = Button(text="Store", width=36, command=store_pass)
store_pass_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()