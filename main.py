# Created by Achyut Jadhav

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_list = [random.choice(letters) for _ in range(nr_letters)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]
    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = letters_list + symbols_list + numbers_list

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_save = website_name.get()
    email_save = email_input.get()
    password_save = password_input.get()
    new_data = {
        web_save: {
            "email": email_save,
            "password": password_save,
        }
    }

    if len(web_save) == 0 or len(password_save) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave field empty")
    else:
        try:
            with open("Password_data.json", "r") as datafile:
                # reading old data
                data = json.load(datafile)
                # updating old data with new data
        except:
            with open("Password_data.json", "w") as datafile:
                json.dump(new_data, datafile, indent=4)
        else:
            data.update(new_data)

            with open("Password_data.json", "w") as datafile:
                json.dump(data, datafile, indent=4)

        finally:
            messagebox.showinfo(title=web_save, message="Password has been saved successfully")
            website_name.delete(0, "end")
            password_input.delete(0, "end")


def find_password():
    web_save = website_name.get()
    try:
        with open("Password_data.json", "r") as datafile:
            info = json.load(datafile)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if web_save in info:
            email = info[web_save]["email"]
            password = info[web_save]["password"]
            messagebox.showinfo(title=web_save, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {web_save} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg='light cyan')

canvas = Canvas(width=200, height=200, bg='light cyan')
photo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

# text on screen
web = Label(text="Website:", bg='light cyan')
web.grid(row=1, column=0)

email = Label(text="Email/Username:", bg='light cyan')
email.grid(row=2, column=0)

password = Label(text="Password:", bg='light cyan')
password.grid(row=3, column=0)

# buttons

generate_p = Button(text="Generate Password", command=generate_password)
generate_p.grid(row=3, column=2)

add = Button(text="Add", width=44, command=save)
add.grid(row=4, column=1, columnspan=2)

search = Button(text="Search", width=14, command=find_password)
search.grid(row=1, column=2)

# input boxes
website_name = Entry(width=33)
website_name.grid(row=1, column=1)
website_name.focus()

email_input = Entry(width=52)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "Achyut@gmail.com")

password_input = Entry(width=33)
password_input.grid(row=3, column=1)

mainloop()
