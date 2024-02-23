import socket
import threading
import json
from database import Database  # Supposons que vous avez une classe Database pour interagir avec la base de données

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.db = Database()  # Initialisez votre base de données ici

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Serveur démarré sur {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Nouvelle connexion de {client_address}")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    break
                # Traitez les données reçues du client
                # Exemple: analyser les données JSON
                data_dict = json.loads(data.decode('utf-8'))
                # Enregistrez les messages dans la base de données
                self.db.save_message(data_dict['channel'], data_dict['user'], data_dict['message'])
                # Envoyer un accusé de réception au client
                client_socket.send("Message reçu et enregistré.".encode('utf-8'))
            except Exception as e:
                print(f"Erreur lors du traitement des données du client : {e}")
                break

    def stop(self):
        self.server_socket.close()
        print("Serveur arrêté.")
