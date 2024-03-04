import tkinter as tk
from client import Client
from chat import Chat
from PIL import Image, ImageTk

class Signin(tk.Frame):
    def __init__(self, master, client):
        tk.Frame.__init__(self, master)
        self.client = client
        
        master.geometry("420x520")
        self.configure(bg="#424549")