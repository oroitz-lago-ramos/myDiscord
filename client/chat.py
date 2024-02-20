import tkinter as tk
import client
import server
import datetime

class Chat:
    def __init__(self, client):
        # On instancie nos classes à déplacer
        self.client = client
        self.database = self.client.database
        self.user = server.User("test","test", self.database)
        self.channel = server.Channel(self.database)
        self.message = server.Message(self.database)
        self.channel_id = 1
        
        self.root = self.client.root
        self.root.title("Server rooms")
        self.root.geometry("1080x720")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=4)

        # Creer deux boites
        #gauche-
        self.channels_frame = tk.Frame(self.root, bg=client.MAIN_COLOR)

        self.channels_list = tk.Listbox(self.channels_frame, bg=client.MAIN_COLOR, fg="white", activestyle="none")
        for channel_name in self.channel.get_channels():
            self.channels_list.insert(tk.END, f"#{channel_name}")
        self.channels_list.pack(fill="both", expand=True)

        self.channels_frame.grid(row=0, column=0, sticky="nsew")
        
        #droite
        chat_frame = tk.Frame(self.root, bg=client.SECONDARY_COLOR)
        self.messages_list = tk.Listbox(chat_frame, bg=client.SECONDARY_COLOR, fg="white", activestyle="none")
        # Le channel 1 est sélectionné par défaut, on affiche les messages de ce channel
        for message in self.message.load_messages_from_channel(1):
            self.messages_list.insert(tk.END, f"{message['user_name']}: {message['content']}")
        
        
        self.messages_list.pack(fill="both", expand=True)

        self.enter_message_box_var = tk.StringVar()
        self.enter_message_box_var.set("Entrez votre message")
        enter_message_box = tk.Entry(chat_frame, bg=client.SECONDARY_COLOR, fg="white", insertbackground="white", textvariable=self.enter_message_box_var)
        enter_message_box.pack(fill="both")

        submit_button = tk.Button(chat_frame, text="Envoyer", command=self.send_message, bg=client.SECONDARY_COLOR, fg="white", activebackground=client.MAIN_COLOR, activeforeground="white")
        submit_button.pack(fill="both")

        chat_frame.grid(row=0, column=1, sticky="nsew")
        
        # self.chat_scroll = tk.Scrollbar(chat_frame)
        # self.chat_scroll.pack()

        self.channels_list.bind("<<ListboxSelect>>", self.update_messages)
        
    def run(self):
        self.root.mainloop()
    
    def send_message(self):
        message = self.enter_message_box_var.get()
        self.channel_id = self.get_selected_channel_id()
        print(self.channel_id)
        print(message)
        if message and self.channel_id:
            self.message.send_message(message, datetime.datetime.now(), self.user.get_user_id(), self.channel_id )
            self.enter_message_box_var.set("")
        self.update_messages()
        
    def update_messages(self,event=None):
        self.channel_id = self.get_selected_channel_id()
        self.messages_list.delete(0, tk.END)
        for message in self.message.load_messages_from_channel(self.channel_id):
            self.messages_list.insert(tk.END, f"  {message['user_name']}: {message['content']}")
                    
    def refresh_messages(self):
        self.update_messages()
        self.root.after(1000, self.refresh_messages)
                      
    def get_selected_channel(self):
        selected_index = self.channels_list.curselection()
        if selected_index:
            selected_channel = self.channels_list.get(selected_index)
            return selected_channel
        return None
    
    def get_selected_channel_id(self):
        selected_index = self.channels_list.curselection()
        if selected_index:
            selected_channel = self.channels_list.get(selected_index)
            channel_id = self.channel.get_channel_id(selected_channel[1:])[0][0]
            return channel_id
        else:
            return 1
    
    