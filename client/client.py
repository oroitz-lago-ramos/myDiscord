import socket
import json

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print("Connecté au serveur.")
        except Exception as e:
            print(f"Impossible de se connecter au serveur : {e}")
    
    def send_message(self, channel, user, message):
        data = {
            'channel': channel,
            'user': user,
            'message': message
        }
        try:
            self.client_socket.send(json.dumps(data).encode('utf-8'))
            response = self.client_socket.recv(1024).decode('utf-8')
            print("Réponse du serveur :", response)
        except Exception as e:
            print(f"Erreur lors de l'envoi du message : {e}")

    def close(self):
        self.client_socket.close()
        print("Connexion au serveur fermée.")
