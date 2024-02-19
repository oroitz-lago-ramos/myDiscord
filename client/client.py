import client
import tkinter as tk

class Client:
    def __init__(self,database):
        self.database = database
        self.root = tk.Tk()
        self.chat = client.Chat(self)
    
    def run(self):
        self.chat.run()
    