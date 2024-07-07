from tkinter import *
import tkinter.messagebox as tkm
import ast

root = Tk()
root.title("Calculator")
photo = PhotoImage(file = "calculator.png")
root.iconphoto(False, photo)
root.geometry("360x330")
i = 0

# -------------------   Functions   ------------------------


def get_num(num):
    global i
    display.insert(i, num)
    i += 1


def get_operation(ope):
    global i
    display.insert(i, ope)
    i += len(ope)


def clear_all():
    display.delete(0, END)


def calculate():
    entire_string = display.get()
    try:
        node = ast.parse(entire_string, mode="eval")
        result = eval(compile(node, '<string>', 'eval'))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()

        tkm.showerror("Error", "Something went wrong")

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_str = entire_string[:-1]
        clear_all()
        display.insert(0, new_str)
    else:
        clear_all()
        display.insert(0, "")


display = Entry(root,font="arial 20 bold")
display.grid(row=1, columnspan=9)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0
for x in range(3):
    for y in range(3):
        btn_txt = num[count]
        button = Button(root, text=btn_txt, width=7, height=4, command=lambda text=btn_txt: get_num(text), bg="pale turquoise", borderwidth=2)
        button.grid(row=x + 2, column=y)
        count += 1

button = Button(root, text="0", width=7, height=4, command=lambda: get_num(0))
button.grid(row=5, column=1)

ope_count = 0
operations = ["+", "-", "*", "/", "*3.14", "%", "(", "**", ")", "**2"]
for a in range(4):
    for b in range(3):
        if ope_count < len(operations):
            button1 = Button(root, text=operations[ope_count], width=7, height=4, command=lambda operator = operations[ope_count]:get_operation(operator), bg="lawn green", borderwidth=2)
            ope_count += 1
            button1.grid(row=a + 2, column=b + 3)


Button(root, text="AC", width=7, height=4, command=clear_all, bg="red", borderwidth=2).grid(row=5, column=0)
Button(root, text="=", width=7, height=4, command=calculate, bg="maroon1", borderwidth=2).grid(row=5, column=2)
Button(root, text="<-", width=16, height=4, command=lambda: undo(), bg="hot pink", borderwidth=2).grid(row=5, column=4, columnspan=2)


root.mainloop()
