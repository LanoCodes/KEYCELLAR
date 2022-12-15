from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json

messagebox.showinfo(message="WELCOME TO KEY-CELLAR.")
# PASSWORD GENERATOR
def gen_pass():
    """Generates password, copies it to clipboard, and populates entry field for saving"""

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]

    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)
    password = ""
    messagebox.showinfo(message="PASSWORD COPIED.")

# SAVE PASSWORD
def store_pass():
    """Adds data entered into fields and stores the text in a file 'data.txt'"""

    site = (website_entry.get()).lower()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        site: {
            "email": email,
            "password": password
        }
    }

    # Checking to make sure that the fields aren't empty when trying to save to file
    if len(site) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as pass_data:
                # Reads old data
                data = json.load(pass_data)
        except FileNotFoundError:
            with open("data.json", "w") as pass_data:
                # When file doesn't exist, above line creates it and writes new_data to it
                json.dump(new_data, pass_data, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as pass_data:
                # Saving updated data
                json.dump(data, pass_data, indent=4)
        finally:
            # No matter what, clear the contents of the entries
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def find_password():
    query = (website_entry.get()).lower()
    try:
        with open("data.json", "r") as pass_data:
            data = json.load(pass_data)
    except FileNotFoundError:
        messagebox.showinfo(message=f"No Data File Found")
    else:
        if query in data:
            messagebox.showinfo(title=query, message=f"Username: {data[query]['email']}\n Password:{data[query]['password']}")
        else:
            messagebox.showinfo(message="No details for that website was found!")


# UI SETUP
window = Tk()
window.title("KEY-CELLAR")
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
website_entry = Entry(width=18)
website_entry.grid(row=1, column=1)
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

# Button to search for a password
search_pass_btm = Button(text="Search", width=10, command=find_password)
search_pass_btm.grid(row=1, column=2)

window.mainloop()