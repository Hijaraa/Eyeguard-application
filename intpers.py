from customtkinter import *
from PIL import Image
from tkinter import *
from PIL import Image, ImageTk
app=CTk()
app.geometry("520x400")
app.title("personel")
app.configure(bg="#57a1f8", fg="white")
set_appearance_mode("light")
#img= Image.open("message_icon.png")
#button
frame = Frame(app, width=520, height=400, bg="#57a1f8")
frame.place(x=0,y=0)
btn = CTkButton(frame, text="logout", text_color= "#57a1f8", fg_color="white",command=lambda: open_intr())
btn.place(relx=0.04, rely =0.1)


def open_intr():
    app.destroy()
    os.system('python login.py')


frame = Frame(app, width=350, height=250, bg="#57a1f8")
frame.place(x=180,y=170)
label = CTkLabel(app, text="personnel",text_color="white", fg_color="#57a1f8", font=("Arial",20))


label.place(relx=0.7, rely=0.05, anchor=CENTER)


# Create an image object from a file
image = Image.open("2.png")

# Convert the image object to a PhotoImage object
photo = ImageTk.PhotoImage(image)

# Create a Label widget to display the image
image_label = Label(app, image=photo,width=80,height=100)
image_label.place(x=180, y=50)


label = CTkLabel(frame, text="Full Name:")
label.place(relx=0.1, rely=0.2, anchor=CENTER)

Full_name_entry = CTkEntry(frame, width=250)
Full_name_entry.place(relx=0.6, rely=0.2, anchor=CENTER)

CTkLabel(frame, text="Matricule:").place(relx=0.1, rely=0.4, anchor=CENTER)
matricule_entry = CTkEntry(frame, width=250)
matricule_entry.place(relx=0.6, rely=0.4, anchor=CENTER)

CTkLabel(frame, text="Email:").place(relx=0.1, rely=0.6, anchor=CENTER)
email_entry = CTkEntry(frame, width=250)
email_entry.place(relx=0.6, rely=0.6, anchor=CENTER)

CTkLabel(frame, text="Age:").place(relx=0.1, rely=0.8, anchor=CENTER)
age_entry = CTkEntry(frame, width=250)
age_entry.place(relx=0.6, rely=0.8, anchor=CENTER)
btn = CTkButton(frame, text="save",width=60,  fg_color="#2B31B6")
btn.place(relx=0.8, rely =0.89)
#checkbox
#checkbox = CTkCheckBox(master=app, text="option")
#checkbox.place(relx=0.5, rely =0.2)

app.mainloop()