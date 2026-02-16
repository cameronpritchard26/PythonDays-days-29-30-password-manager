import tkinter as tk
from tkinter import messagebox
import secrets
import string
import json
import pyperclip
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv("DEFAULT_EMAIL")


# ---------------------------- FIND PASSWORD ----------------------------------- #
def search():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No information found")
    else:
        website = website_entry.get()
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
        else:
            messagebox.showerror(title="Error", message=f"No information for {website} found")
        

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    valid_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(valid_chars) for _ in range(16))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_information():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "" or email == "" or password == "":
        messagebox.showerror(title="Error", message="Please fill in all fields")
    else:
        msg = f"Website: {website}\nEmail: {email}\nPassword: {password}"
        is_ok = messagebox.askokcancel(title="Confirmation", message=f"Entered information:\n{msg}\n\nIs this correct?")
        if is_ok:
            entry_data = {website: {"email": email, "password": password}}
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(entry_data)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(entry_data, data_file, indent=4)
            else:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            messagebox.showinfo(title="Success", message="Password saved successfully")
            website_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            email_entry.insert(0, EMAIL)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = tk.Canvas(window, width=200, height=200)
logo_img = tk.PhotoImage(file="images/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


website_label = tk.Label(window, text="Website:")
website_label.grid(row=1, column=0)

website_entry = tk.Entry(window, width=55)
website_entry.grid(row=1, column=1)
website_entry.focus()

website_button = tk.Button(window, text="Search", width=15, command=search)
website_button.grid(row=1, column=2)


email_label = tk.Label(window, text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = tk.Entry(window, width=74)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, EMAIL)


password_label = tk.Label(window, text="Password:")
password_label.grid(row=3, column=0)

password_entry = tk.Entry(window, width=55)
password_entry.grid(row=3, column=1)

password_button = tk.Button(window, text="Generate Password", width=15, command=generate_password)
password_button.grid(row=3, column=2)


add_button = tk.Button(window, text="Add", width=63, command=save_information)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
