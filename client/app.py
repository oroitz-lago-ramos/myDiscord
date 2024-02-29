import tkinter as tk
from client import Client
from login import Login
from chat import Chat
from threading import Thread

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.MAIN_COLOR = "#424549"
        self.SECONDARY_COLOR = "#36393e"
        
        self._frame = None
        
        self.client = Client()
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.switch_frame(Login)
        
        
 
    def switch_frame(self, frame_class, email=None):
        if email is not None:
            new_frame = frame_class(self, self.client, email)  # Pass the email to the frame_class constructor
            if self._frame is not None:
                self._frame.destroy()
            self._frame = new_frame
            self._frame.grid(sticky='nsew')
        else:
            new_frame = frame_class(self, self.client)
            if self._frame is not None:
                self._frame.destroy()
            self._frame = new_frame
            self._frame.grid(sticky='nsew')
        

app = App()
app.mainloop()