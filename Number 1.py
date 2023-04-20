import tkinter as tk

root = tk.Tk()

root.geometry("400x150")
root.title("Label")
first_sentence = "Laboratory Activity 5"
second_sentence = "Submitted to: Ma'am Sayo"

display_text = f"{first_sentence}\n{second_sentence}"

display_label = tk.Label(root, text=display_text, font=("Arial", 14), pady=20)

display_label.pack(side="top", fill="both", expand=True)

root.mainloop()
