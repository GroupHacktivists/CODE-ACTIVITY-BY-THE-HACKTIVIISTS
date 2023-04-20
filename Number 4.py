from tkinter import *
import random


class MyWindow:
    def __init__(self, win):
        self.win = win
        self.cb = Button(win, text="Change Color", font="Verdana 10", bg="black", fg="red",
                         activebackground=random.choice(['#FFFF00', '#0000FF']), command=self.change_color)
        self.cb.place(x=50, y=100)
        self.color_text = Label(win, text="<------------Click to Change Color", font="Verdana 8", bg="#FFFFFF", fg="black")
        self.color_text.place(x=160, y=105)

    def change_color(self):
        hex_colors = ['#FFFF00', '#0000FF']  # yellow and blue hex colors
        hex_color = random.choice(hex_colors)
        self.cb.config(bg=hex_color, activebackground=hex_color)


window = Tk()
mywin = MyWindow(window)
window.geometry("500x200+10+10")
window.title("Button")
window.mainloop()
