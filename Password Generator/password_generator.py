import string
import random
from tkinter import *
import tkinter.messagebox as message

root = Tk()
root.geometry("300x300")
root.title("Password Generator")
leng_val = IntVar()
pass_val = StringVar()


def generatePass():
    # length = int(input(" Enter the length of password :- "))
    length = leng_val.get()
    if length != 0:
        password = ran = ''.join(
            random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=length))
        # print("The password is :", str(password))
        pass_label.config(text="The password is:-" + password)
        pass_label.grid(row=2, columnspan=2)
    else:
        message.showerror("Error", "Please give the password Length")


# --------------  Widgets
label = Label(root, text="Length of Password")
label.grid(row=0, column=0)

entry_box = Entry(root, textvariable=leng_val, )
entry_box.grid(row=0, column=1)

genbutton = Button(root, text='Generate', command=generatePass)
genbutton.grid(row=1, columnspan=2)

pass_label = Label(root)

root.mainloop()
