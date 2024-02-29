import tkinter as tk
from client import Client
from chat import Chat

# Create a window
window = tk.Tk()
window.geometry("420x520")
window.configure(bg="#424549")

# Create email and password entry fields
email_entry = tk.Entry(window)
email_entry.pack()

password_entry = tk.Entry(window)
password_entry.pack()

# Run the tkinter event loop
window.mainloop()