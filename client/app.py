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
        
        # self.client = Client()
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.switch_frame(Login)
        
        
 
    def switch_frame(self, frame_class):
        new_frame = frame_class(self, None)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid(sticky='nsew')

        

    # def switch_channel(self):
    #     channel_id = int(self.channel_entry.get())
    #     self.client.switch_channel(channel_id)
    #     self.display_messages()

    # def display_messages(self):
    #     messages = self.client.load_messages()
    #     self.text_area.delete('1.0', tk.END)  # Clear the text area
    #     for message in messages:
    #         self.text_area.insert(tk.END, f"{message[1]}: {message[0]}\n")

    # def send_message(self):
    #     message = self.message_entry.get()
    #     self.client.send_chat_message('oroitz@gmail.com', message)  # Replace 'user@example.com' with the actual user email

    

app = App()
app.mainloop()