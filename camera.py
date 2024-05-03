import tkinter as tk
from customtkinter import * 
import cv2
import PIL.Image, PIL.ImageTk



class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        set_appearance_mode("dark")
        self.vid = MyVideoCapture(self.video_source)
        
        self.canvas = tk.Canvas(window, width = 400, height = 300)
        self.canvas.pack()
        
        #self.btn_snapshot=tk.Button(window, text="login", width=20,height=2, command=self.snapshot )
        self.btn_snapshot=tk.Button(window, text="login", width=20,height=2, command=lambda: os.system('python login.py'))
        self.btn_snapshot.pack(anchor=tk.CENTER, expand=True)
        
        self.delay = 15
        self.update()
        
        self.window.mainloop()

    def snapshot(self):
        ret, frame = self.vid.get_frame()
        
        if ret:
            cv2.imwrite("snapshot.png", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    
    def update(self):
        ret, frame = self.vid.get_frame()
        
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tk.NW)
        
        self.window.after(self.delay, self.update)

class MyVideoCapture:
    def __init__(self, video_source=0):
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)
        
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (False, None)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

App(tk.Tk(), "camera")