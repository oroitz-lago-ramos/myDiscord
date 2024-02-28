import tkinter as tk
from client import Client
from chat import Chat

class Login(tk.Frame):
    def __init__(self, master, client):
        tk.Frame.__init__(self, master)
        # self.client = client

        master.geometry("420x520")
        self.configure(bg="#424549")

        self.create_widgets()

    def create_widgets(self):
        email_label = tk.Label(self, text="Email", bg="#424549", fg="white")
        email_label.pack(pady=(150, 0))
        email_entry = tk.Entry(self)
        email_entry.pack(pady=10)

        password_label = tk.Label(self, text="Password", bg="#424549", fg="white")
        password_label.pack(pady=10)
        password_entry = tk.Entry(self, show="*")
        password_entry.pack(pady=10)

        login_button = tk.Button(self, text="Connexion")
        login_button.pack(pady=10)

        signin_button = tk.Button(self, text="Sign in")
        signin_button.pack(pady=10)
