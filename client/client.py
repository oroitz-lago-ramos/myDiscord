import socket
import json

class Client:
    """
    La classe Client sert a gerer la connexion avec le serveur. Il envoie et recoit des messages du serveur.
    """
    def __init__(self, host='127.0.0.1', port=55555):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

    def send_message(self, message):
        """
        Envoie un message au serveur
        """
        self.client.send(message.encode('utf-8'))
    def receive_message(self):
        """
        Recoit un message du serveur
        """
        try:
            message = self.client.recv(20000).decode('utf-8')
            return message
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    def receive_loop_message(self):
        """
        Recoit un message du serveur
        """
        try:
            self.client.settimeout(2)  #Timeout de 2 secondes
            message = self.client.recv(8000).decode('utf-8')
            return message
        except socket.timeout:
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def switch_channel(self, channel_id):
        """
        Envoie une commande au serveur pour changer de channel
        """
        self.send_message(f'switch_channel > {channel_id}')

    def send_chat_message(self, user, message):
        """
        Envoi in message de chat au serveur
        """
        self.send_message(f'message > {message}')
    
    def load_messages(self):
        """
        Envoie une commande au serveur pour charger les messages du channel actuel
        """
        self.send_message('load_messages')
        messages_str = self.receive_message()
        if messages_str:
            messages = json.loads(messages_str)
        else:
            messages = []
        return messages

    def load_channels(self):
        """
        Envoie une commande au serveur pour charger les channels
        """
        self.send_message('load_channels')
        channels_str = self.receive_message()
        if channels_str:
            channels = json.loads(channels_str)
        else:
            channels = []
        return channels
    
    def login(self, email, password):
        """
        Envoie une commande au serveur pour se connecter
        """
        self.send_message(f'login > {email} > {password}')
        response = self.receive_message()
        print(f"Client received: {response}")
        if response == 'login_success':
            return True
        else:
            return False
        
    def create_user(self, lastname, name, email, password):
        """
        Envoie une commande au serveur pour creer un utilisateur
        """
        self.send_message(f'create_user > {lastname} > {name} > {email} > {password}')
        response = self.receive_message()
        print(f"Client received: {response}")
        if response == 'user_created':
            return True
        else:
            return False