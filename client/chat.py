import tkinter as tk
import client

class Chat_screen:
    def __init__(self):
        # Ne pas créer le root ici juste pour test
        self.root = tk.Tk()
        self.root.title("Server rooms")
        self.root.geometry("1080x720")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=4)

        # Creer deux boites
        #gauche-
        channels_frame = tk.Frame(self.root, bg=client.MAIN_COLOR)

        channels_list = tk.Listbox(channels_frame, bg=client.MAIN_COLOR, fg="white", activestyle="none")
        # for channel_name in channel.get_channels():
        #     channels_list.insert(tk.END, channel_name)
        channels_list.pack(fill="both", expand=True)

        channels_frame.grid(row=0, column=0, sticky="nsew")
        
        #droite
        chat_frame = tk.Frame(self.root, bg=client.SECONDARY_COLOR)
        messages_list = tk.Listbox(chat_frame, bg=client.SECONDARY_COLOR, fg="white", activestyle="none")
        # for message in message.load_messages_from_channel(1):
        #     messages_list.insert(tk.END, f"{message['user_name']}: {message['content']}")
        messages_list.pack(fill="both", expand=True)

        enter_message_box_var = tk.StringVar()
        enter_message_box_var.set("Entrez votre message")
        enter_message_box = tk.Entry(chat_frame, bg=client.SECONDARY_COLOR, fg="white", insertbackground="white", textvariable=enter_message_box_var)
        enter_message_box.pack(fill="both")

        submit_button = tk.Button(chat_frame, text="Envoyer", command=self.send_message, bg=client.SECONDARY_COLOR, fg="white", activebackground=client.MAIN_COLOR, activeforeground="white")
        submit_button.pack(fill="both")

        chat_frame.grid(row=0, column=1, sticky="nsew")
        
        # self.chat_scroll = tk.Scrollbar(chat_frame)
        # self.chat_scroll.pack()


        
    def run(self):
        self.root.mainloop()
    
    def send_message(self):
        # message = self.entry_box.get()
        # self.chat_list.insert(tk.END, message)
        # self.entry_box.delete(0, tk.END)
        print("clicked")
    
    