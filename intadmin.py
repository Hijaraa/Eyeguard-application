


from customtkinter import *
from PIL import Image
from tkinter import *
from PIL import Image, ImageTk
app=CTk()
app.geometry("550x430")
set_appearance_mode("light")
app.title("Admin")
#frame = Frame(app, width=300, height=400, bg="#0F1545")
#frame.place(x=45,y=0)
#combobox = CTkComboBox(master=app, values=[ "Add" ,"Student","Visitor","Personel"],  fg_color="#2B31B6")
#combobox.place(relx=0.04, rely =0.2)
#label
#label = CTkLabel(master=app, text="txt", font=("Arial",20))
#label.place(relx=0.9, rely =0.5)
#combobox
#combobox = CTkComboBox(master=app, values=[ "Update" ,"Student","Visitor","Personel"],  fg_color="#2B31B6")
#combobox.place(relx=0.04, rely =0.3)

#combobox = CTkComboBox(master=app, values=[ "Delete" ,"Student","Visitor","Personel"],  fg_color="#2B31B6")
#combobox.place(relx=0.04, rely =0.4)

#combobox = CTkComboBox(master=app, values=[ "Search" ,"Student","Visitor","Personel"],  fg_color="#2B31B6")
#combobox.place(relx=0.04, rely =0.5)

#combobox = CTkComboBox(master=app, values=[ "Other" ,"Mouvement","Alert"],  fg_color="#2B31B6")
#combobox.place(relx=0.04, rely =0.6)

#btn = CTkButton(frame, text="logout" , fg_color="#2B31B6",command=lambda: os.system('python login.py'))
btn = CTkButton(app, text="Student", fg_color="#57a1f8",width=300,height=50,command=lambda: open_stu())
btn.place(relx=0.2, rely =0.1)
btn = CTkButton(app, text="Visitor", fg_color="#57a1f8",width=300,height=50,command=lambda: open_vis())
btn.place(relx=0.2, rely =0.2)
btn = CTkButton(app, text="Personnel", fg_color="#57a1f8",width=300,height=50,command=lambda: open_per())
btn.place(relx=0.2, rely =0.3)
btn = CTkButton(app, text="Mouvement in reel time ", fg_color="#57a1f8",width=300,height=50,command=lambda: open_movrt())
btn.place(relx=0.2, rely =0.4)
btn = CTkButton(app, text="Abnormal mouvement", fg_color="#57a1f8",width=300,height=50,command=lambda: open_abnmv())
btn.place(relx=0.2, rely =0.5)
btn = CTkButton(app, text="logout", fg_color="#57a1f8",command=lambda: open_intr())
btn.place(relx=0.07, rely =0.9)

#frame = Frame(app, width=350, height=250, bg="#020627")
#frame.place(x=180,y=150)

def open_intr():
    app.destroy()
    os.system('python login.py')

def open_stu():
    app.destroy()
    os.system('python etudiant.py')

def open_vis():
    app.destroy()
    os.system('python visitor.py')

def open_per():
    app.destroy()
    os.system('python personnel.py')

def open_movrt():
    app.destroy()
    os.system('python admmov.py')

def open_abnmv():
    app.destroy()
    os.system('python movanor.py')    



# Create an image object from a file
#image = Image.open("2.png")

# Convert the image object to a PhotoImage object
#photo = ImageTk.PhotoImage(image)

# Create a Label widget to display the image
#image_label = Label(app, image=photo,width=90,height=120)
#image_label.place(x=180, y=20)


#label = CTkLabel(frame, text="Full Name:")
#label.place(relx=0.1, rely=0.2, anchor=CENTER)

#Full_name_entry = CTkEntry(frame, width=250)
#Full_name_entry.place(relx=0.6, rely=0.2, anchor=CENTER)

#CTkLabel(frame, text="Matricule:").place(relx=0.1, rely=0.4, anchor=CENTER)
#matricule_entry = CTkEntry(frame, width=250)
#matricule_entry.place(relx=0.6, rely=0.4, anchor=CENTER)

#CTkLabel(frame, text="Email:").place(relx=0.1, rely=0.6, anchor=CENTER)
#email_entry = CTkEntry(frame, width=250)
#email_entry.place(relx=0.6, rely=0.6, anchor=CENTER)

#CTkLabel(frame, text="Age:").place(relx=0.1, rely=0.8, anchor=CENTER)
#age_entry = CTkEntry(frame, width=250)
#age_entry.place(relx=0.6, rely=0.8, anchor=CENTER)
#checkbox
#checkbox = CTkCheckBox(master=app, text="option")
#checkbox.place(relx=0.5, rely =0.2)
#btn = CTkButton(frame, text="save",width=60,  fg_color="#2B31B6")
#btn.place(relx=0.8, rely =0.89)
app.mainloop()



