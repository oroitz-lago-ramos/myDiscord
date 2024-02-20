import client
import tkinter as tk

class Client:
    def __init__(self,database):
        self.database = database
        self.root = tk.Tk()
        self.login = client.Login(self)
        self.signin = client.Signin(self)
        self.chat = client.Chat(self)
        
        
    
    def run(self):
        self.chat.run()
    