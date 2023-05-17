import tkinter as tk
from tkinter import ttk, messagebox
import sys

from tkinter import *
import os

def delete2():
    screen3.destroy()

def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()

def login_success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text = "Login Success").pack()
    Button(screen3, text = "OK", command = delete2).pack()


def password_not_recognized():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Error")
    screen4.geometry("150x100")
    Label(screen4, text="Incorrect Password").pack()
    Button(screen4, text="OK", command=delete3).pack()
    messagebox.showerror("Error", "Incorrect Password")
    sys.exit(0)

def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Error")
    screen5.geometry("150x100")
    Label(screen5, text="User Unrecognized").pack()
    Button(screen5, text="OK", command=delete4).pack()
    messagebox.showerror("Error", "User Unrecognized")
    sys.exit(0)

def register_users():
    print("working")
    username_info = username.get()
    password_info = password.get()

    file=open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete (0, END)
    password_entry.delete (0, END)

    Label (screen1, text = "Registration Succesful", fg = "green", font = ("calibri", 11)).pack()

def login_verify():

    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognized()
    else:
        user_not_found()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("500x350")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()



    Label(screen1, text = "Please enter details below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username *").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password *").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width = 10, height= 1, command = register_users).pack()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("500x350")

    Label(screen2, text = "Please enter details below to login").pack()
    Label(screen2, text = "").pack()

    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text = "Username *").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Password *").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("500x350")
    screen.title("Hacktivist Bank")
    Label(text = "WELCOME TO HACKTIVIST CO.",width = 300, height = 2, bg = "light blue", font = ("Calibri", 13)).pack()
    Label(text = "", ).pack()
    Button(text = "Log In", width = 50, height = 2, command = login).pack()
    Label(text = "", ).pack()
    Button(text = "Register", width = 50, height = 2, command = register).pack()

    screen.mainloop()

main_screen()

class BankSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank System")

        # Create style
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 12))
        style.configure("TEntry", font=("Helvetica", 12))
        style.configure("TButton", font=("Helvetica", 12))

        # Create labels
        self.label_balance = ttk.Label(root, text="Balance:")
        self.label_balance.grid(row=0, column=0, padx=10, pady=10)

        # Create entry fields
        self.entry_balance = ttk.Entry(root)
        self.entry_balance.grid(row=0, column=1, padx=10, pady=10)

        # Create buttons
        self.button_deposit = ttk.Button(root, text="Deposit", command=self.deposit)
        self.button_deposit.grid(row=1, column=0, padx=10, pady=10)

        self.button_withdraw = ttk.Button(root, text="Withdraw", command=self.withdraw)
        self.button_withdraw.grid(row=1, column=1, padx=10, pady=10)

        self.button_check_balance = ttk.Button(root, text="Check Balance", command=self.check_balance)
        self.button_check_balance.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Set initial balance
        self.balance = 0

    def deposit(self):
        amount = self.entry_balance.get()

        if amount:
            try:
                amount = float(amount)
                if amount > 0:
                    self.balance += amount
                    messagebox.showinfo("Success", "Deposit successful.")
                else:
                    messagebox.showerror("Error", "Please enter a positive amount.")
            except ValueError:
                messagebox.showerror("Error", "Invalid amount.")
        else:
            messagebox.showerror("Error", "Please enter an amount.")

        self.entry_balance.delete(0, tk.END)

    def withdraw(self):
        amount = self.entry_balance.get()

        if amount:
            try:
                amount = float(amount)
                if amount > 0:
                    if self.balance >= amount:
                        self.balance -= amount
                        messagebox.showinfo("Success", "Withdrawal successful.")
                    else:
                        messagebox.showerror("Error", "Insufficient balance.")
                else:
                    messagebox.showerror("Error", "Please enter a positive amount.")
            except ValueError:
                messagebox.showerror("Error", "Invalid amount.")
        else:
            messagebox.showerror("Error", "Please enter an amount.")

        self.entry_balance.delete(0, tk.END)

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is: {self.balance}")


# Create the root window
root = tk.Tk()

# Create an instance of the BankSystemGUI
bank_system_gui = BankSystemGUI(root)

# Run the main event loop
root.mainloop()
