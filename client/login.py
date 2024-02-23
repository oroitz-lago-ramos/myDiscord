import tkinter as tk
from client import Client
from chat import Chat

class Login(tk.Frame):
    def __init__(self, master, client):
        tk.Frame.__init__(self, master)
        self.client = client

        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Send the username and password to the server
        self.client.send_message(f"LOGIN {username} {password}")

        # Wait for a response from the server
        response = self.client.receive_message()

        if response == "LOGIN SUCCESS":
            # If the login was successful, switch to the Chat page
            self.master.switch_frame(Chat)

