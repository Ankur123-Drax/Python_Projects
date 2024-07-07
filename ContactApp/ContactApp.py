from tkinter import *
import tkinter.messagebox as message
import mysql.connector as mysql

root = Tk()
root.title("Contact Book App")
root.geometry("700x500")

icon_img = PhotoImage(file="images/contact.png")
root.iconphoto(FALSE, icon_img)


#  -------------------  Functions  ---------------
def add_contact():
    name = name_ent.get()
    phone = phone_ent.get()
    email = email_ent.get()
    address = address_ent.get()
    phone2 = phone2_ent.get()
    if name == "" or phone == "" or email == "" or address == "":
        message.showinfo("Insert Status", "All Fields are required")
    else:

        conn = mysql.connect(host="localhost", user="root", password="", database="contact_book_app")
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO `contactlist`(`name`, `phone1`, `email`, `address`, `phone2`) VALUES ('"+name+"','"+phone+"','"+email+"','"+address+"','"+phone2+"')")
            cursor.execute("commit")
            name_ent.delete(0, 'end')
            phone_ent.delete(0, 'end')
            email_ent.delete(0, 'end')
            address_ent.delete(0, 'end')
            phone2_ent.delete(0, 'end')
            message.showinfo("Insert Status", "Inserted Successfully")
            conn.close()
        except Exception as e:
            message.showerror("Error Occurred", "Error: '"+e+"'")


def search_contact():
    email = email_search_ent.get()
    phone = phone_search_ent.get()

    if phone == "" or email == "":
        message.showinfo("Search Status", "All Fields are required")
    else:
        conn = mysql.connect(host="localhost", user="root", password="", database="contact_book_app")
        cursor = conn.cursor()
        try:
            cursor.execute(
                "SELECT * FROM `contactlist` WHERE email='" + email + "' AND phone1='" + phone + "'")
            phone_search_ent.delete(0, 'end')
            email_search_ent.delete(0, 'end')
            row = cursor.fetchall()
            data = []
            for item in row:
                for n in range(5):
                    data.append(item[n])
            message.showinfo("Search Status", "Search Successful")
            result_label.config(text=data)
            cursor.execute("commit")
            conn.close()
        except Exception as e:
            message.showerror("Error Occurred", "Error :'" + str(e) + "'")


def update_contact():
    name = name_ent.get()
    phone = phone_ent.get()
    phone2 = phone2_ent.get()
    email = email_ent.get()
    address = address_ent.get()
    if name == "" or phone == "" or email == "" or address == "":
        message.showinfo("Update Status", "All Fields are required")
    else:
        conn = mysql.connect(host="localhost", user="root", password="", database="contact_book_app")
        cursor = conn.cursor()
        try:
            cursor.execute(
                "UPDATE `contactlist` SET `name`='"+name+"',`phone1`='"+phone+"',`email`='"+email+"',`address`='"+address+"',"
                "`phone2`='"+phone2+"' WHERE email='"+email+"' AND phone1='"+phone+"' ")

            name_ent.delete(0, 'end')
            phone_ent.delete(0, 'end')
            email_ent.delete(0, 'end')
            address_ent.delete(0, 'end')
            phone2_ent.delete(0, 'end')
            message.showinfo("Update Status", "Updated Successfully")
            cursor.execute("commit")
            conn.close()
        except Exception as e:
            message.showerror("Error Occurred", "Error :'" + str(e) + "'")


def delete_contact():
    email = email_search_ent.get()
    phone = phone_search_ent.get()

    if phone == "" or email == "":
        message.showinfo("Search Status", "All Fields are required")
    else:
        conn = mysql.connect(host="localhost", user="root", password="", database="contact_book_app")
        cursor = conn.cursor()
        try:
            cursor.execute(
                "DELETE FROM `contactlist` WHERE email= '" + email + "' AND phone1='" + phone + "'")
            cursor.execute("commit")
            phone_search_ent.delete(0, 'end')
            email_search_ent.delete(0, 'end')
            message.showinfo("Delete Status", "Deleted Successfully")
            conn.close()
        except EXCEPTION as e:
            message.showerror("Error Occurred", "Error ::'" + str(e) + "'")


#  ---------------- menu Frame Function -----------------

def menu_add():
    welcome_label.place_forget()
    view_frame.place_forget()
    frame2.place_forget()
    frame1.place(x=150, y=70)
    add_con_button.config(text="Add Contact", command=add_contact)


def menu_view():
    welcome_label.place_forget()
    frame1.place_forget()
    frame2.place_forget()
    view_frame.place(x=150, y=70)
    conn = mysql.connect(host="localhost", user="root", password="", database="contact_book_app")
    cursor = conn.cursor()
    cursor.execute("select * from contactlist ")
    rows = cursor.fetchall()
    x = 0
    for row in rows:
        name = Label(view_frame, text=row[0], width=6, font="arial 8 bold", bg="white", )
        name.place(x=0, y=50 + x)
        phone1 = Label(view_frame, text=row[1], width=12, font="arial 8 bold", bg="white", )
        phone1.place(x=55, y=50 + x)
        phone2 = Label(view_frame, text=row[4], width=12, font="arial 8 bold", bg="white", )
        phone2.place(x=160, y=50 + x)
        email = Label(view_frame, text=row[2], width=22, font="arial 8 bold", bg="white", )
        email.place(x=280, y=50 + x)
        address = Label(view_frame, text=row[3], width=11, font="arial 8 bold", bg="white", )
        address.place(x=450, y=50 + x)
        x += 30


def menu_search():
    welcome_label.place_forget()
    frame1.place_forget()
    frame2.place(x=150, y=70)


def menu_update():
    welcome_label.place_forget()
    view_frame.place_forget()
    frame2.place_forget()
    frame1.place(x=150, y=70)
    add_con_button.config(text="Update Contact", command=update_contact)


def menu_delete():
    welcome_label.place_forget()
    view_frame.place_forget()
    frame1.place_forget()
    frame2.place(x=150, y=70)
    add_search_button.config(text="Delete Contact", command=delete_contact)


#  ------------------  Header  ---------------------

header = PhotoImage(file="images/header1.png")
Label(root, image=header, ).pack(fill=X)

icon1 = PhotoImage(file="images/contact1.png")
Label(root, image=icon1, bg="#00A2E8").place(x=190, y=4)

appName = Label(root, text="Save Your Contact", font="arial 20 bold", fg="white", bg="#00A2E8", bd=2)
appName.place(x=250, y=12)

#  -------- Frame ----------------
menu_frame = Frame(root, width=150, height=400, bg="#00A2E8", bd=5)
menu_frame.place(x=0, y=70)

frame1 = Frame(root, width=540, height=400, bg="white")

view_frame = Frame(root, width=540, height=400, bg="#00A2E8", bd=5)

frame2 = Frame(root, width=540, height=400, bg="white", bd=5)
#  ---------------- Widgets  ----------------------

name_label = Label(frame1, text="Name :", font="arial 15 bold", bg="white", fg="#00A2E8")
name_label.place(x=20, y=20)

phone_label = Label(frame1, text="PhoneNum :", font="arial 15 bold", bg="white", fg="#00A2E8")
phone_label.place(x=20, y=60)

phone_2_label = Label(frame1, text="PhoneNum2 :", font="arial 15 bold", bg="white", fg="#00A2E8")
phone_2_label.place(x=20, y=100)

email_label = Label(frame1, text="Email :", font="arial 15 bold", bg="white", fg="#00A2E8")
email_label.place(x=20, y=140)

address_label = Label(frame1, text="Address :", font="arial 15 bold", bg="white", fg="#00A2E8")
address_label.place(x=20, y=180)

name_var = StringVar()
name_ent = Entry(frame1, width=25, font="arial 20", bd=4)
name_ent.place(x=150, y=21)

phone_var = IntVar()
phone_ent = Entry(frame1, width=25, font="arial 20", bd=4)
phone_ent.place(x=150, y=61)

phone2_var = IntVar()
phone2_ent = Entry(frame1, width=25, font="arial 20", bd=4)
phone2_ent.place(x=150, y=101)

email_var = StringVar()
email_ent = Entry(frame1, width=25, font="arial 20", bd=4)
email_ent.place(x=150, y=141)

address_var = StringVar()
address_ent = Entry(frame1, width=25, font="arial 20", bd=4)
address_ent.place(x=150, y=181)

add_con_button = Button(frame1, text="ADD CONTACT", font="arial 15 bold", fg="#00A2E8", bg="white", bd=4,
                        command=add_contact)
add_con_button.place(x=370, y=230)

#  --------------- Menu Frame Widgets  --------------

add_button = Button(menu_frame, text="ADD", width=10, font="arial 15 bold", fg="#00A2E8", bg="white", bd=2,
                    command=menu_add)
add_button.place(x=4, y=10)

view_contact_button = Button(menu_frame, text="VIEW", width=10, font="arial 15 bold", fg="#00A2E8", bg="white", bd=2,
                             command=menu_view)
view_contact_button.place(x=4, y=55)

search_button = Button(menu_frame, text="SEARCH", width=10, font="arial 15 bold", fg="#00A2E8", bg="white", bd=2,
                       command=menu_search)
search_button.place(x=4, y=100)

update_button = Button(menu_frame, text="UPDATE", width=10, font="arial 15 bold", fg="#00A2E8", bg="white", bd=2,
                       command=menu_update)
update_button.place(x=4, y=145)

delete_button = Button(menu_frame, text="DELETE", width=10, font="arial 15 bold", fg="#00A2E8", bg="white", bd=2,
                       command=menu_delete)
delete_button.place(x=4, y=190)

#  ------------ View frame widgets --------------
name2_label = Label(view_frame, text="Name |", font="arial 10 bold", bg="white", fg="#00A2E8")
name2_label.place(x=0, y=20)

phone2_label = Label(view_frame, text="Phone Number1 |", font="arial 10 bold", bg="white", fg="#00A2E8")
phone2_label.place(x=55, y=20)

phone2_2_label = Label(view_frame, text="Phone Number2 |", font="arial 10 bold", bg="white", fg="#00A2E8")
phone2_2_label.place(x=170, y=20)

email2_label = Label(view_frame, text="Email |", font="arial 10 bold", bg="white", fg="#00A2E8")
email2_label.place(x=290, y=20)

address2_label = Label(view_frame, text="Address |", font="arial 10 bold", bg="white", fg="#00A2E8")
address2_label.place(x=450, y=20)

# -   --          ------------------ Search frame widgets--------------------

email_label = Label(frame2, text="Email :", font="arial 15 bold", bg="white", fg="#00A2E8")
email_label.place(x=20, y=20)
phone_label = Label(frame2, text="PhoneNum :", font="arial 15 bold", bg="white", fg="#00A2E8")
phone_label.place(x=20, y=60)

email_search_var = StringVar()
email_search_ent = Entry(frame2, width=25, font="arial 20", bd=4)
email_search_ent.place(x=150, y=21)

phone_search_var = IntVar()
phone_search_ent = Entry(frame2, width=25, font="arial 20", bd=4)
phone_search_ent.place(x=150, y=61)

add_search_button = Button(frame2, text="Search Contact", font="arial 15 bold", fg="#00A2E8", bg="white", bd=4,
                           command=search_contact)
add_search_button.place(x=363, y=110)

result_label = Label(frame2, font="arial 10 bold", bg="#00A2E8", fg="white")
result_label.place(x=0, y=160)


welcome_label = Label(root, text="Welcome to Contact Book App", font="arial 25 bold", fg="#00A2E8", bg="white")
welcome_label.place(x=170, y=170)

root.mainloop()
