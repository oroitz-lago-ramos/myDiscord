import tkinter as tk
import server

class MyDiscord():
    def run(self):

        database = server.Database()
        message = server.Message(database)
        channel = server.Channel(database)



        def send_message():
            message = enter_message_box_var.get()
            if message:
                messages_list.insert(tk.END, f"{pseudo1}: {message}")
                enter_message_box_var.set("")

        # pyqt? kivy? tkinter?
        MAIN_COLOR = "#424549"
        SECONDARY_COLOR = "#36393e"
        pseudo1 = "Pseudo1"
        pseudo2 = "Pseudo2"

        # Create a window
        window = tk.Tk()
        window.title("MyDiscord")
        window.geometry("1080x720")

        #configuration des tailles du grid
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        window.grid_columnconfigure(1, weight=4)
        # Creer deux boites
        #gauche-
        subframe = tk.Frame(window, bg=MAIN_COLOR)

        channels_list = tk.Listbox(subframe, bg=MAIN_COLOR, fg="white", activestyle="none")
        for channel_name in channel.get_channels():
            channels_list.insert(tk.END, channel_name)
        channels_list.pack(fill="both", expand=True)

        subframe.grid(row=0, column=0, sticky="nsew")
        #droite
        subframe2 = tk.Frame(window, bg=SECONDARY_COLOR)


        messages_list = tk.Listbox(subframe2, bg=SECONDARY_COLOR, fg="white", activestyle="none")
        messages_list.insert(0, "Bienvenue sur le chat")
        for message in message.load_messages_from_channel(1):
            messages_list.insert(tk.END, f"{message['user_name']}: {message['content']}")
        messages_list.pack(fill="both", expand=True)

        enter_message_box_var = tk.StringVar()
        enter_message_box_var.set("Entrez votre message")
        enter_message_box = tk.Entry(subframe2, bg=SECONDARY_COLOR, fg="white", insertbackground="white", textvariable=enter_message_box_var)
        enter_message_box.pack(fill="both")

        submit_button = tk.Button(subframe2, text="Envoyer", command=send_message, bg=SECONDARY_COLOR, fg="white", activebackground=MAIN_COLOR, activeforeground="white")
        submit_button.pack(fill="both")

        subframe2.grid(row=0, column=1, sticky="nsew")





        window.mainloop()
        
