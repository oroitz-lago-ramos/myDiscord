import tkinter as tk
from chat import Chat
from PIL import Image, ImageTk

class Signin(tk.Frame):
    def __init__(self, master, client):
        tk.Frame.__init__(self, master)
        self.client = client
        
        master.title("Create Account")
        master.geometry("420x520")
        self.configure(bg="#424549")

        # self.image = Image.open("discord3.png")
        # self.image = self.image.resize((200, 200))
        # self.photo = ImageTk.PhotoImage(self.image)
        # self.image_label = tk.Label(self, image=self.photo, bg="#424549")
        # self.image_label.pack()

        # self.image_label.pack()

        self.name_label = tk.Label(self, text="Name:" , bg="#424549", fg="white")
        self.name_label.pack()
        self.name_entry = tk.Entry(self)
        self.name_entry = tk.Entry(self,)
        self.name_entry.pack(pady=(15, 0))
        
        self.lastname_label = tk.Label(self, text="Last Name:", bg="#424549", fg="white")
        self.lastname_label.pack()
        self.lastname_entry = tk.Entry(self)
        self.lastname_entry.pack(pady=(15, 0))
        
        self.email_label = tk.Label(self, text="Email:", bg="#424549", fg="white")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=(15, 0))
        
        self.password_label = tk.Label(self, text="Password:", bg="#424549", fg="white")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=(15, 0))
        
        self.create_button = tk.Button(self, text="Create Account", command=self.create_account)
        self.create_button.pack(pady=10)
        
    def create_account(self):
        lastname = self.lastname_entry.get()
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        
        if self.client.create_user(lastname, name, email, password):
            self.master.switch_frame(Chat, email)
        else:
            print("Account creation failed")
        
     
    
    
        
        
