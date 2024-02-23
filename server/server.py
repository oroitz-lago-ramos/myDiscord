import socket
import threading
import json
from database import Database
from user import User
from message import Message
from channel import Channel

import datetime

class Server:
    def __init__(self, host = '127.0.0.1', port = 55555):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()

        self.clients = []
        
        self.database = Database()
        self.user = User(self.database)
        self.message = Message(self.database)
        self.channel = Channel(self.database)

        self.user_email = "oroitz@gmail.com"  # Add this line
        self.channel_id = None  # Add this line

    # Add these methods to set the current user and channel
    def set_current_user(self, user_email):
        self.user_email = user_email

    def set_current_channel(self, channel_id):
        self.channel_id = channel_id
        print(f"Switched to channel {channel_id}")

    # Then, in your handle method, you can use self.user_email and self.channel_id
    def handle(self, client):
        while True:
            try:
                message = client.recv(1024).decode('ascii')
                if ' > ' in message:
                    command, data = message.split(' > ', 1)

                    if command == 'switch_channel':
                        self.set_current_channel(int(data))
                    elif command == 'message':
                        msg = data
                        time = datetime.datetime.now()
                        user_id = self.user.get_id(self.user_email)
                        channel_id = self.channel_id
                        print(f"Received message from {user_id}: {msg}")
                        # self.broadcast(msg, self.user_email)
                        self.message.send_message(msg, time, user_id, channel_id)
                    elif command == 'create_user':
                        
                        self.user.create_user(data)
                elif message == 'load_messages':
                    messages = self.message.load_messages_from_channel(self.channel_id)
                    messages_str = json.dumps(messages)
                    client.sendall(messages_str.encode('utf-8'))
                else:
                    print(f"Received unformatted message: {message}")
            except Exception as e:
                print(f"An error occurred: {e}")
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                break

    def receive(self):
        while True:
            client, address = self.server.accept()
            self.clients.append(client)

            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()
    def broadcast(self, message, user):
        for client in self.clients:
            client.send(f'{user}: {message}'.encode('ascii'))
        
if __name__ == "__main__":
    my_server = Server()
    my_server.receive()