import tkinter
from tkinter import *
from tkinter.ttk import *

screen = Tk()
screen.geometry("800x800")  # size
screen.configure(background="#7AC5CD")  # color
screen.title("sign up for volunteer project")

def INPUT_BOX(text,row,col):
    title = tkinter.Label(screen, text=text,background="#7AC5CD",foreground="#6A5ACD",font=("Times",18),anchor=NW).grid(row=row, column=col)
    input = tkinter.Entry(screen, bd=7, width=55).grid(row=row, column=col+1)


def open_success_signin():
    newWindow = Toplevel(screen, background="#7AC5CD")
    newWindow.geometry("800x300")
    Label(newWindow,
          text="Thank you so much for signing up! we appreciate it !", foreground="#6A5ACD", background="#7AC5CD",
          font=("Times", 25)).pack(pady=100)

def open_inputs_signin():
    INPUT_BOX("enter your name: ",1,1)
    INPUT_BOX("enter a description of your contribution: ",2,1)
    INPUT_BOX("How can we contact you? enter email or phone number: ",3,1)
    INPUT_BOX("In which area would you like to contribute? ",4,1)
    INPUT_BOX("Tell us your specialization: ",5,1)

# tkinter.Label(screen, text="Enter a discription of the service you offer: ").grid(row=1)
# name_box = tkinter.Entry(screen)
# screen.create_window(200, 140, window=name_box)
#general_title.pack(pady=120)
def open_final_submit():
    general_title = tkinter.Label(screen, text="join us to Volunteer in any area you want and help youth at risk",
                                  foreground="#6A5ACD", background="#7AC5CD", font=("Times", 20))
    general_title.pack(pady=120)
    btn = tkinter.Button(screen, text="make the world a better place", foreground="#7AC5CD", font=("Times", 15),
                     background="#6A5ACD", command=open_success_signin)
    btn.configure()
    btn.pack(pady=100)

#open_final_submit()
open_inputs_signin()
mainloop()




subjects_of_service = {}

print("do you want to volunteer for youth at Risk?")

#     subject = input("In which area would you like to contribute? ")
#     if subject not in subjects_of_service:
#         subjects_of_service[subject]={}
#     print("Tell us your specialization: ")
#     sub_theme = input()
#     if sub_theme not in subjects_of_service[subject]:
#         dict_sub= subjects_of_service[subject][sub_theme]=[]
#     subjects_of_service[subject][sub_theme].append([volunteer_name,description,contact])
