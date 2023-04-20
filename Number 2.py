import tkinter as tk

# Create the main window
root = tk.Tk()

root.geometry("300x150")


# Set the window title
root.title("Text Field")

# Define the title string
title = "This is where I type my text"

# Create a text entry widget with the title as default text
text_entry = tk.Entry(root, font=("Arial", 12), width=21)
text_entry.insert(0, title)
text_entry.pack(pady=65)

# Start the main loop
root.mainloop()
