import tkinter as tk

class Chat(tk.Frame):
    def __init__(self, master, client):
        tk.Frame.__init__(self, master)
        self.client = client

        master.title("myDiscord - Server rooms")
        master.geometry("1080x720")

        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=4)

        # Create two boxes
        # Left
        self.channels_frame = tk.Frame(master, bg=client.MAIN_COLOR)
       
        self.channels_list = tk.Listbox(self.channels_frame, bg=client.MAIN_COLOR, fg="white", activestyle="none")
        self.channels_list.pack(fill="both", expand=True)
        
        self.channels_frame.grid(row=0, column=0, sticky="nsew")
        
        #right
        self.chat_frame = tk.Frame(self.root, bg=client.SECONDARY_COLOR)
        self.messages_list = tk.Listbox(self.chat_frame, bg=client.SECONDARY_COLOR, fg="white", activestyle="none")
        self.messages_list.pack(fill="both", expand=True)
        
        self.enter_message_box_var = tk.StringVar()
        self.enter_message_box_var.set("Entrez votre message...")
        enter_message_box = tk.Entry(self.chat_frame, bg=client.SECONDARY_COLOR, fg="white", insertbackground="white", textvariable=self.enter_message_box_var)
        enter_message_box.pack(fill="both")
        
        submit_button = tk.Button(self.chat_frame, text="Envoyer", command=self.send_message, bg=client.SECONDARY_COLOR, fg="white", activebackground=client.MAIN_COLOR, activeforeground="white")
        submit_button.pack(fill="both")
        
        self.chat_frame.grid(row=0, column=1, sticky="nsew")