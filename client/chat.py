import tkinter as tk
import client
import threading


class Chat(tk.Frame):
    def __init__(self, master, client):
        tk.Frame.__init__(self, master)
        self.client = client
        

        master.title("myDiscord - Server rooms")
        master.geometry("1080x720")

        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=5)

        # Create two boxes
        # Left
        self.channels_frame = tk.Frame(master, bg=master.MAIN_COLOR)
        self.channels_frame.grid(row=0, column=0, sticky="nsew")

        self.channels_list = tk.Listbox(self.channels_frame, bg=master.MAIN_COLOR, fg="white", activestyle="none")
        self.display_channels()
        self.channels_list.pack(fill="both", expand=True)

        # Right
        self.chat_frame = tk.Frame(master, bg=master.SECONDARY_COLOR)
        self.chat_frame.grid(row=0, column=1, sticky="nsew")

        self.messages_list = tk.Listbox(self.chat_frame, bg=master.SECONDARY_COLOR, fg="white", activestyle="none")
        self.display_messages()
        self.messages_list.pack(fill="both", expand=True)

        self.enter_message_box_var = tk.StringVar()
        self.enter_message_box_var.set("Entrez votre message...")
        enter_message_box = tk.Entry(self.chat_frame, bg=master.SECONDARY_COLOR, fg="white", insertbackground="white", textvariable=self.enter_message_box_var)
        enter_message_box.pack(fill="both")

        submit_button = tk.Button(self.chat_frame, text="Envoyer", command=self.send_message, bg=master.SECONDARY_COLOR, fg="white", activebackground=master.MAIN_COLOR, activeforeground="white")
        submit_button.pack(fill="both")
        
        self.chat_frame.grid(row=0, column=1, sticky="nsew")
        
        
        self.start_listening()
        
        enter_message_box.bind("<FocusIn>", self.clear_message_box)
        enter_message_box.bind("<FocusOut>", self.reset_message_box)  
        enter_message_box.bind("<Return>", lambda event: self.send_message())
        self.channels_list.bind("<<ListboxSelect>>", self.switch_channel)
    
    def switch_channel(self,event):
        index = self.channels_list.curselection()[0]
        self.client.switch_channel(index + 1)
        self.display_messages()

    def display_messages(self):
        messages = self.client.load_messages()
        self.messages_list.delete(0, tk.END)  # Clear the text area
        for message in messages:
            self.messages_list.insert(tk.END, f" {message[1]}: {message[0]}\n")
    
    
    def display_channels(self):
        channels = self.client.load_channels()
        for channel in channels:
            self.channels_list.insert(tk.END, f"#{channel[1]}")
        

    def send_message(self):
        message = self.enter_message_box_var.get()
        self.client.send_chat_message('oroitz@gmail.com', message)
        self.clear_message_box(None)
        
    def start_listening(self):
        listen_thread = threading.Thread(target=self.listen_for_messages)
        listen_thread.daemon = True  # Set the thread as daemon so it will exit when the main thread exits
        listen_thread.start()

    def listen_for_messages(self):
        while True:
            message = self.client.receive_loop_message() 
            if message:
                self.messages_list.insert(tk.END, message)
    
    def clear_message_box(self, event):
        self.enter_message_box_var.set("")
    
    def reset_message_box(self, event):
        self.enter_message_box_var.set("Entrez votre message...")
        