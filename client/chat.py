import tkinter as tk
import client
import threading


class Chat(tk.Frame):
    """
    Ecran de chat
    """
    def __init__(self, master, client, email):
        tk.Frame.__init__(self, master)
        self.client = client
        self.email = email
        

        master.title("myDiscord - Server rooms")
        master.geometry("1080x720")

        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=5)

        # Creation de deux frames, une pour la liste des channels et une pour les messages
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
        """
        Sert à changer le channel selectionné dans la liste des channels et affiche les messages du nouveau channel
        """
        index = self.channels_list.curselection()[0]
        self.client.switch_channel(index + 1)
        self.display_messages()

    def display_messages(self):
        """
        Charge les messages du channel actuel et les affiche dans la liste des messages
        """
        messages = self.client.load_messages()
        self.messages_list.delete(0, tk.END)  # Reset la liste des messages
        for message in messages:
            self.messages_list.insert(tk.END, f" {message[2]} - {message[1]}: {message[0]}\n")
    
    
    def display_channels(self):
        """
        Charge les channels et les affiche dans la liste des channels
        """
        channels = self.client.load_channels()
        for channel in channels:
            self.channels_list.insert(tk.END, f"#{channel[1]}")
        

    def send_message(self):
        """
        Envoie un message au serveur à partir du contenu de la boite de message à travers le client
        """
        message = self.enter_message_box_var.get()
        self.client.send_chat_message(self.email, message)
        self.clear_message_box(None)
        
    def start_listening(self):
        """
        Demarre un thread pour ecouter les messages du serveur en continue
        """
        listen_thread = threading.Thread(target=self.listen_for_messages)
        listen_thread.daemon = True  # Le thread s'arrete lorsque le programme principal s'arrete
        listen_thread.start()

    def listen_for_messages(self):
        """
        Ecoute les messages du serveur en continue et les affiche dans la liste des messages
        """
        while True:
            message = self.client.receive_loop_message() 
            if message:
                self.messages_list.insert(tk.END, message)
    
    def clear_message_box(self, event):
        """
        Efface le contenu de la boite de message
        """
        self.enter_message_box_var.set("")
    
    def reset_message_box(self, event):
        """
        Remet le contenu de la boite de message à sa valeur par defaut
        """
        self.enter_message_box_var.set("Entrez votre message...")
        