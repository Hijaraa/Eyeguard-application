import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
from customtkinter import *
def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['id'])
    e2.insert(0,select['empname'])
    e3.insert(0,select['mobile'])
    e4.insert(0,select['email'])


def Add():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="database")
    mycursor=mysqldb.cursor()

    try:
       sql = "INSERT INTO  registation (id,empname,mobile,email) VALUES (%s, %s, %s, %s)"
       val = (studid,studname,coursename,feee)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Student inserted successfully...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()


def update():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="database")
    mycursor=mysqldb.cursor()

    try:
       sql = "Update  registation set empname= %s,mobile= %s,email= %s where id= %s"
       val = (studname,coursename,feee,studid)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "databaseord Updateddddd successfully...")

       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()

    except Exception as e:

       print(e)
       mysqldb.rollback()
       mysqldb.close()

def delete():
    studid = e1.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="database")
    mycursor=mysqldb.cursor()

    try:
       sql = "delete from registation where id = %s"
       val = (studid,)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "databaseord Deleteeeee successfully...")

       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()

    except Exception as e:

       print(e)
       mysqldb.rollback()
       mysqldb.close()

def show():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="database")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT id,empname,mobile,email FROM registation")
        databaseords = mycursor.fetchall()
        print(databaseords)

        for i, (id,stname, course,fee) in enumerate(databaseords, start=1):
            listBox.insert("", "end", values=(id, stname, course, fee))
            mysqldb.close()

root = CTk()

root.geometry("800x500")

root.title("Student")
global e1
global e2
global e3
global e4

#tk.Label(root, text="Student Registation", fg="red", font=(None, 30)).place(x=300, y=5)

label = CTkLabel(root, text="Student ID").place(x=10, y=10)
label = CTkLabel(root, text="Student Name").place(x=10, y=40)
label = CTkLabel(root, text="Mobile").place(x=10, y=70)
label = CTkLabel(root, text="Email").place(x=10, y=100)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=70)

e4 = Entry(root)
e4.place(x=140, y=100)

btn = CTkButton(root, text="Add",  fg_color="#2B31B6",command = Add ).place(x=30, y=140)
btn = CTkButton(root, text="Update",  fg_color="#2B31B6",command = update ).place(x=180, y=140)
btn = CTkButton(root, text="Delete", fg_color="#2B31B6",command = delete ).place(x=330, y=140)
btn = CTkButton(root, text="Back",  fg_color="#2B31B6",command=lambda: open_inta())
btn.place(x=580, y =140)

def open_inta():
    root.destroy()
    os.system('python intadmin.py')

cols = ('id', 'empname', 'mobile','email')
listBox = ttk.Treeview(root, columns=cols, show='headings' )

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)

show()
listBox.bind('<Double-Button-1>',GetValue)

root.mainloop()