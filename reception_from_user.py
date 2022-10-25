from tkinter import *
import volunteer_page

def make_button(subject):
    root = Tk()
    root.geometry('500x500')
    btn = Button(root, text=subject, bd='10',
                 command=volunteer_page.open_window)
    btn.pack(side='top')
    root.mainloop()

make_button("math")