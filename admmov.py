from customtkinter import *
from PIL import Image
from tkinter import *
from PIL import Image, ImageTk
app=CTk()
app.geometry("520x400")
app.title("Movement")
set_appearance_mode("light")
frame = Frame(app, width=180, height=400, bg="white")
frame.place(x=0,y=0)

#label
#label = CTkLabel(master=app, text="txt", font=("Arial",20))
#label.place(relx=0.9, rely =0.5)
#combobox
btn = CTkButton(frame, text="Mouvement",  fg_color="#57a1f8")
btn.place(relx=0.07, rely =0.1)

#btn = CTkButton(frame, text="Alert",  fg_color="#2B31B6")
#btn.place(relx=0.07, rely =0.5)

btn = CTkButton(frame, text="Back",  fg_color="#57a1f8",command=lambda: open_inta())
btn.place(relx=0.07, rely =0.8)

btn = CTkButton(frame, text="logout",  fg_color="#57a1f8",command=lambda: open_intr())
btn.place(relx=0.07, rely =0.9)

def open_intr():
    app.destroy()
 

def open_inta():
    app.destroy()
    os.system('python intadmin.py')

frame = Frame(app, width=350, height=400, bg="#57a1f8")
frame.place(x=180,y=0)

#frames = Frame(app, width=350, height=195, bg="#020627")
#frames.place(x=180,y=0)

#label = CTkLabel(frames, text="Full Name:")
#label.place(relx=0.1, rely=0.2, anchor=CENTER)

#Full_name_entry = CTkEntry(frames, width=250)
#Full_name_entry.place(relx=0.6, rely=0.2, anchor=CENTER)

#label = CTkLabel(frames, text="Type:")
#label.place(relx=0.1, rely=0.4, anchor=CENTER)

#Full_name_entry = CTkEntry(frames, width=250)
#Full_name_entry.place(relx=0.6, rely=0.4, anchor=CENTER)
# Create an image object from a file
#image = Image.open("2.png")

# Convert the image object to a PhotoImage object
#photo = ImageTk.PhotoImage(image)

# Create a Label widget to display the image
#image_label = Label(app, image=photo,width=90,height=120)
#image_label.place(x=180, y=20)
label = CTkLabel(frame, text="Full Name:")
label.place(relx=0.1, rely=0.2, anchor=CENTER)

Full_name_entry = CTkEntry(frame, width=250)
Full_name_entry.place(relx=0.6, rely=0.2, anchor=CENTER)

label = CTkLabel(frame, text="Space:")
label.place(relx=0.1, rely=0.4, anchor=CENTER)

Full_name_entry = CTkEntry(frame, width=250)
Full_name_entry.place(relx=0.6, rely=0.4, anchor=CENTER)

#checkbox
#checkbox = CTkCheckBox(master=app, text="option")
#checkbox.place(relx=0.5, rely =0.2)
#btn = CTkButton(frame, text="save",width=60,  fg_color="#2B31B6")
#btn.place(relx=0.8, rely =0.89)
app.mainloop()



