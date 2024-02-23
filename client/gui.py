import tkinter as tk
from client import Client
from threading import Thread

class App:
    def __init__(self, root):
        self.client = Client()

        self.channel_entry = tk.Entry(root)
        self.channel_entry.pack()

        self.switch_button = tk.Button(root, text="Switch Channel", command=self.switch_channel)
        self.switch_button.pack()

        self.message_entry = tk.Entry(root)
        self.message_entry.pack()

        self.send_button = tk.Button(root, text="Send Message", command=self.send_message)
        self.send_button.pack()

        self.text_area = tk.Text(root)
        self.text_area.pack()

        

    def switch_channel(self):
        channel_id = int(self.channel_entry.get())
        self.client.switch_channel(channel_id)
        self.display_messages()

    def display_messages(self):
        messages = self.client.load_messages()
        self.text_area.delete('1.0', tk.END)  # Clear the text area
        for message in messages:
            self.text_area.insert(tk.END, f"{message[1]}: {message[0]}\n")

    def send_message(self):
        message = self.message_entry.get()
        self.client.send_chat_message('oroitz@gmail.com', message)  # Replace 'user@example.com' with the actual user email

    
        
root = tk.Tk()
app = App(root)
root.mainloop()