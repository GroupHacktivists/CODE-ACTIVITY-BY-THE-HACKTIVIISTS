from tkinter import *


class MyWindow:
    def __init__(self, win):
        self.title1 = Label(win, text="Charles Babbage", font=("Verdana", 20), bg="#00FFFF")
        self.title1.place(x=100, y=75)


window = Tk()
mywin = MyWindow(window)
window.geometry("400x200+10+10")
window.title("Father of Computer")
window.mainloop()