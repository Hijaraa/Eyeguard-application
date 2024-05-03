import mysql.connector
from tkinter import *
from tkinter import messagebox
import ast

root = Tk()
root.title("login form")
root.geometry("925x500+300+200")
root.resizable(False, False)

def signin():
    username = user.get()
    password = code.get()

    file = open('datasheet.txt', 'r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    print(r.keys())
    print(r.values())

    if username in r.keys() and password == r[username]:
        screen = Toplevel(root)
        screen.title("app")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")
        Label(screen, text='hi').pack(expand=True)
        screen.mainloop()
    else:
        messagebox.showerror("invalid", "invalid user or pass")

def signup_command():
    def signup():
        username = user.get()
        password = code.get()
        confirm_password = confirm_code.get()
        email = email_entry.get()
        age = age_entry.get()

        if password == confirm_password:
            try:
                conn = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='password',
                    database='test_db'
                )
                c = conn.cursor()
                c.execute('''CREATE TABLE IF NOT EXISTS users (username text, password int, email text, age integer)''')
                c.execute("INSERT INTO users VALUES (?,?,?,?)", (username, password, email, age))
                conn.commit()
                conn.close()
                messagebox.showinfo('signup', 'successfuly signup')
            except mysql.connector.Error as err:
                messagebox.showerror('Error', err)
        else:
            messagebox.showerror('invalid', "error")

    window = Toplevel(root)
    window.title("signup form")
    window.geometry("925x500+300+200")
    window.resizable(False, False)

    img = PhotoImage(file='2.png')
    img = img.subsample(3)

    Label(window, image=img, bg="white").place(x=50, y=50)

    frame = Frame(window, width=390, height=450, bg="white")
    frame.place(x=480, y=25)

    heading = Label(frame, text="sign up", fg="#57a1f8", bg="white", font=('Microsoft YaHei UILight', 23, 'bold'))
    heading.place(x=100, y=20)
    def on_enter(e):
        user.delete(0, 'end')
    def on_leave(e):
        if user.get() == '':
            user.insert(0, 'username')

    user = Entry(frame, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UILight', 11))
    user.place(x=30, y=80)
    user.insert(0, 'username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

    def on_enter(e):
        code.delete(0, 'end')
    def on_leave(e):
        if code.get() == '':
            code.insert(0, 'Password')

    code = Entry(frame, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UILight', 11))
    code.place(x=30, y=150)
    code.insert(0, 'password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

    def on_enter(e):
        confirm_code.delete(0, 'end')
    def on_leave(e):
        if confirm_code.get() == '':
            confirm_code.insert(0, 'confirm Password')

    confirm_code = Entry(frame, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UILight', 11))
    confirm_code.place(x=30, y=220)
    confirm_code.insert(0, 'confirm password')
    confirm_code.bind('<FocusIn>', on_enter)
    confirm_code.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=247)

    def on_enter(e):
        email_entry.delete(0, 'end')
    def on_leave(e):
        if email_entry.get() == '':
            email_entry.insert(0, 'Email')

    email_entry = Entry(frame, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UILight', 11))
    email_entry.place(x=30, y=280)
    email_entry.insert(0, 'Email')
    email_entry.bind('<FocusIn>', on_enter)
    email_entry.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg="black").place(x=30, y=300)

    def on_enter(e):
        age_entry.delete(0, 'end')
    def on_leave(e):
        if age_entry.get() == '':
            age_entry.insert(0, 'age')

    age_entry = Entry(frame, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UILight', 11))
    age_entry.place(x=30, y=330)
    age_entry.insert(0, 'age')
    age_entry.bind('<FocusIn>', on_enter)
    age_entry.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg="black").place(x=30, y=350)

    Button(frame, width=39, pady=7, text="sign up", bg="#57a1f8", fg="white", border=0, cursor="hand2", command=signup).place(x=35, y=360)
    label = Label(frame, text="i have an account", fg="black", bg="white", font=('Microsoft YaHei UILight', 9))
    label.place(x=90, y=400)
    sign_in = Button(frame, width=6, text="sign in", fg="#57a1f8", bg="white", border=0 ,cursor="hand2", command=window.destroy)
    sign_in.place(x=190, y=400)

    window.mainloop()

img = PhotoImage(file='2.png')
img = img.subsample(3)

Label(root, image=img, bg="white").place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=50)

heading = Label(frame, text="sign in", fg="#57a1f8", bg="white", font=('Microsoft YaHei UILight', 23, 'bold'))
heading.place(x=100, y=20)

def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'username')

user = Entry(frame, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UILight', 11))
user.place(x=30, y=80)
user.insert(0, 'username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

def on_enter(e):
    code.delete(0, 'end')
def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')

code = Entry(frame, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UILight', 11))
code.place(x=30, y=150)
code.insert(0, 'password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

Button(frame, width=39, pady=7, text="sign in", bg="#57a1f8", fg="white", border=0, cursor="hand2", command=signin).place(x=35, y=204)
label = Label(frame, text="don't have an account?", fg="black", bg="white", font=('Microsoft YaHei UILight', 9))
label.place(x=75, y=270)
sign_up = Button(frame, width=6, text="sign up", fg="#57a1f8", bg="white", border=0, cursor="hand2", command=signup_command)
sign_up.place(x=215, y=270)

root.mainloop()
