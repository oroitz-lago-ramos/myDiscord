import tkinter as tk
from client import Client
from chat import Chat
from PIL import Image, ImageTk

class Login(tk.Frame):
    def __init__(self, master, client):
        tk.Frame.__init__(self, master)
        self.client = client

        master.geometry("420x520")
        self.configure(bg="#424549")
        
        self.error_message = tk.StringVar()  # Create a StringVar to hold the error message
        self.error_label = tk.Label(self, textvariable=self.error_message, fg="red",bg="#424549")  # Create a label to display the error message
        self.error_label.pack()

        self.create_widgets()

    def create_widgets(self):
        image = Image.open("asset/discord3.png")
        image = image.resize((175, 100))
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(self, image=photo)
        image_label.pack(pady=(15,10))

        email_label = tk.Label(self, text="Email", bg="#424549", fg="white")
        email_label.pack(pady=(10, 0))
        email_entry = tk.Entry(self)
        email_entry.pack(pady=10)

        password_label = tk.Label(self, text="Password", bg="#424549", fg="white")
        password_label.pack(pady=10)
        password_entry = tk.Entry(self, show="*")
        password_entry.pack(pady=10)

        login_button = tk.Button(self, text="Connexion", command=lambda: self.attempt_login(email_entry.get(), password_entry.get()))
        login_button.pack(pady=10)

        signin_button = tk.Button(self, text="Sign in")
        signin_button.pack(pady=10)
        
    def attempt_login(self, email, password):
        success = self.client.login(email, password)
        print(success)
        if success:
            self.master.switch_frame(Chat, email)
        else:
            # Show an error message and stay on the login page
            self.error_message.set("Invalid email or password.")
            