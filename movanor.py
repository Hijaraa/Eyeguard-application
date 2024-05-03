from customtkinter import *
from PIL import Image
from tkinter import *
from PIL import Image, ImageTk
app=CTk()
app.title("Abnormal Movement")
app.geometry("520x400")
set_appearance_mode("light")


#label
#label = CTkLabel(master=app, text="txt", font=("Arial",20))
#label.place(relx=0.9, rely =0.5)
#combobox



btn = CTkButton(app, text="Back",  fg_color="#57a1f8",command=lambda: open_inta())
btn.place(relx=0.4, rely =0.9)

btn = CTkButton(app, text="logout",  fg_color="#57a1f8",command=lambda: open_intr())
btn.place(relx=0.7, rely =0.9)


def open_intr():
    app.destroy()
    

def open_inta():
    app.destroy()
    os.system('python intadmin.py')


label = CTkLabel(app, text="Full Name:")
label.place(relx=0.1, rely=0.1, anchor=CENTER)

Full_name_entry = CTkEntry(app, width=250)
Full_name_entry.place(relx=0.6, rely=0.1, anchor=CENTER)

label = CTkLabel(app, text="Type:")
label.place(relx=0.1, rely=0.2, anchor=CENTER)

type_entry = CTkEntry(app, width=250)
type_entry.place(relx=0.6, rely=0.2, anchor=CENTER)

label = CTkLabel(app, text="Date:")
label.place(relx=0.1, rely=0.3, anchor=CENTER)

date_entry = CTkEntry(app, width=250)
date_entry.place(relx=0.6, rely=0.3, anchor=CENTER)



#Create an image object from a file
image = Image.open("2.png")

#Convert the image object to a PhotoImage object
photo = ImageTk.PhotoImage(image)

#Create a Label widget to display the image
image_label = Label(app, image=photo,width=90,height=120)
image_label.place(relx=0.1, rely=0.4)

label = CTkLabel(app, text="Alert:")
label.place(relx=0.1, rely=0.8, anchor=CENTER)

alert_entry = CTkEntry(app, width=250 ,height=50)
alert_entry.place(relx=0.6, rely=0.8, anchor=CENTER)

#checkbox
#checkbox = CTkCheckBox(master=app, text="option")
#checkbox.place(relx=0.5, rely =0.2)
#btn = CTkButton(app, text="save",width=60,  fg_color="#2B31B6")
#btn.place(relx=0.8, rely =0.89)
app.mainloop()



