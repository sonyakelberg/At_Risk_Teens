import lists_DANCE
import tkinter
from tkinter import *

screen = Tk()
screen.geometry("1200x1000")
screen.title("volunteers related to dance")

screen.configure(background="#7AC5CD")  # color
screen.title("volunteers related to dance")
# scrollBar =tkinter.Scrollbar(screen,width= 10)
# scrollBar.pack(expand = True)
# mylist = tkinter.Listbox(screen,yscrollcommand=scrollBar.set)
# a = 150
# for i in range(len(lists_DANCE.dance_content)):
#     a+=50
#     for j in range(len(lists_DANCE.dance_content[i])):
#         if j==0:
#             mylist.insert(END, lists_DANCE.dance_content[i][j])
#             #label = tkinter.Label(screen, text=lists_DANCE.dance_content[i][j], background="#7AC5CD", foreground="#6A5ACD", font=('Times', 25,"bold"))
#         else:
#             mylist.insert(END, lists_DANCE.dance_content[i][j])
#             #label = tkinter.Label(screen, text=lists_DANCE.dance_content[i][j], background="#7AC5CD",
#                                   #foreground="#6A5ACD", font=('Times', 25))
#         a+=50
# mylist.pack(side=LEFT, fill=BOTH)
# scrollBar.config(command=mylist.yview)



def make_title():
    tkinter.Label(screen, text="dance classes", background="#7AC5CD", foreground="#6A5ACD", font=('Times', 60,"bold")).place(x=300, y=0)
    # tkinter.Label(screen, text=lists_DANCE.dance_content, background="#7AC5CD", foreground="#6A5ACD", font=('Times', 35)).place(x=500,
    #                                                                                                             y=100)
    a = 150
    for i in range(len(lists_DANCE.dance_content)):
        a+=50
        for j in range(len(lists_DANCE.dance_content[i])):
            if j==0:
                label = tkinter.Label(screen, text=lists_DANCE.dance_content[i][j], background="#7AC5CD", foreground="#6A5ACD", font=('Times', 25,"bold"))
            else:
                label = tkinter.Label(screen, text=lists_DANCE.dance_content[i][j], background="#7AC5CD",
                                      foreground="#6A5ACD", font=('Times', 25))
            label.place(x=0, y=a)
            a += 50
        label = tkinter.Label(screen, text="", background="#7AC5CD", foreground="#6A5ACD")
        label.place(x=0, y=a)

make_title()
mainloop()
# S = ScrollBar()
