from tkinter import *
import tkinter.messagebox as message

root = Tk()
root.geometry("500x700")
root.resizable(False, False)
root.title("To-Do-List App")

task_list = []


# --------- Functions ------------------

def show_task():
    try:
        with open("allTaskFile.txt", "r") as file:
            tasks = file.readlines()
        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listBox.insert(END, task)
    except Exception as e:
        message.showerror("Error", "'" + str(e) + "'")


def add_task():
    task = task_ent.get()
    desc = desc_ent.get()
    dd = d_d_ent.get()
    if task != "" or desc != "" or dd != "":
        com_task = task + " | " + desc + " | " + dd
        if com_task:
            with open("allTaskFile.txt", 'a') as file:
                file.write(f"\n{com_task}")
            task_list.append(com_task)
            listBox.insert(END, com_task)
        task_ent.delete(0, END)
        desc_ent.delete(0, END)
        d_d_ent.delete(0, END)
    else:
        message.showinfo("Insert Status", "All fields are required !")


def update_task():
    global task_list
    if str(listBox.get(ANCHOR)) != "":
        task = task_ent.get()
        desc = desc_ent.get()
        dd = d_d_ent.get()
        if task != "" or desc != "" or dd != "":
            com_task = task + " | " + desc + " | " + dd
            if com_task:
                with open("allTaskFile.txt", 'a') as file:
                    file.write(f"\n{com_task}")
                task_list.append(com_task)
                listBox.insert(ANCHOR, com_task)
            listBox.delete(ANCHOR)
            task_ent.delete(0, END)
            desc_ent.delete(0, END)
            d_d_ent.delete(0, END)
        else:
            message.showinfo("Insert Status", "All fields are required !")


def del_task():
    global task_list
    task = str(listBox.get(ANCHOR))
    if task in task_list:
        with open("allTaskFile.txt", 'w') as file:
            for task in task_list:
                file.write(task + "\n")

        listBox.delete(ANCHOR)


# ----------

imgIcon = PhotoImage(file="images/to-do-list-apps.png")
root.iconphoto(FALSE, imgIcon)

# -------------
header = PhotoImage(file="images/header.png")
Label(root, image=header).pack(fill=X)

icon1 = PhotoImage(file="images/to-do-list-apps.png")
Label(root, image=icon1, bg="#ED1C24").place(x=150, y=5)

appName = Label(root, text="Tasks List", font="arial 20 bold", fg="white", bg="#ED1C24")
appName.place(x=200, y=10)

# -- ---------- Frame 1  ---------------

frame1 = Frame(root, width=500, height=180, bg="white")
frame1.place(x=0, y=53)

#  -------------  Widgets ------------


taskLabel = Label(frame1, text="Task", font="arial 15 bold", bg="white", fg="red")
taskLabel.place(x=20, y=20)

descLabel = Label(frame1, text="Description", font="arial 15 bold", bg="white", fg="red")
descLabel.place(x=20, y=50)

ddLabel = Label(frame1, text="Due-Date", font="arial 15 bold", bg="white", fg="red")
ddLabel.place(x=20, y=80)

task_var = StringVar()
task_ent = Entry(frame1, width=25, font="arial 15", bd=2)
task_ent.place(x=140, y=21)

desc_var = StringVar()
desc_ent = Entry(frame1, width=25, font="arial 15", bd=2)
desc_ent.place(x=140, y=51)

dd_var = StringVar()
d_d_ent = Entry(frame1, width=25, font="arial 15", bd=2)
d_d_ent.place(x=140, y=81)

addTaskButton = Button(frame1, text="Add Task", font="arial 15 bold", width=10, bg='#ED1C24', fg="#fff", bd=2,
                       command=add_task)
addTaskButton.place(x=100, y=125)

UpdateTaskButton = Button(frame1, text="Update Task", font="arial 15 bold", width=10, bg='#ED1C24', fg="#fff", bd=2,
                          command=update_task)
UpdateTaskButton.place(x=250, y=125)

#  _----------------- New Frame -----------------
frame2 = Frame(root, bd=3, width=500, height=400, bg="red")
frame2.pack(pady=(180, 0))

listBox = Listbox(frame2, font=('arial', 12), width=51, height=20, bg="red", cursor="hand2", selectbackground="#5a95ff")
listBox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(frame2)
scrollbar.pack(side=RIGHT, fill=BOTH)

listBox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listBox.yview)

show_task()

delete_icon = PhotoImage(file="images/delete.png")
del_button = Button(root, image=delete_icon, bd=0, command=del_task)
del_button.pack(side=BOTTOM, pady=13)

root.mainloop()
