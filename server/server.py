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

        self.clients = {}
        
        self.database = Database()
        self.user = User(self.database)
        self.message = Message(self.database)
        self.channel = Channel(self.database)


    # Then, in your handle method, you can use self.user_email and self.channel_id
    def handle(self, client):
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if ' > ' in message:
                    command, data = message.split(' > ', 1)

                    if command == 'switch_channel':
                        channel_id = int(data)
                        self.clients[client]['channel_id'] = channel_id  # Update the client's channel
                    elif command == 'message':
                        user_email = self.clients[client]['user_email']  # Get the client's email
                        channel_id = self.clients[client]['channel_id']  # Get the client's channel
                        msg = data
                        time = datetime.datetime.now()
                        user_id = self.user.get_id(user_email)
                        user_name = self.user.get_user_name(user_id)
                        self.broadcast(msg, user_name, channel_id, time)
                        self.message.send_message(msg, time, user_id, channel_id)
                    elif command == 'create_user':
                        lastname, name, email, password = data.split(' > ', 3)
                        if self.user.user_exists(email):
                            client.send('user_exists'.encode('utf-8'))
                        else:
                            self.user.create_user(lastname, name, email, password)
                            client.send('user_created'.encode('utf-8'))
                    elif command == 'login':
                        email, password = data.split(' > ', 1)
                        if self.user.authenticate(email, password):  # Assuming you have an authenticate method in your User class
                            self.clients[client]['user_email'] = email
                            client.send('login_success'.encode('utf-8'))
                            print("Server sent: login_success")
                        else:
                            client.send('login_fail'.encode('utf-8'))
                            print("Server sent: login_fail")
                elif message == 'load_messages':
                    messages = self.message.load_messages_from_channel(self.clients[client]['channel_id'])
                    messages_str = json.dumps(messages)
                    client.sendall(messages_str.encode('utf-8'))
                    
                elif message == 'load_channels':
                    channels = self.channel.get_channels()
                    channels_str = json.dumps(channels)
                    client.sendall(channels_str.encode('utf-8'))
                else:
                    print(f"Received unformatted message: {message}")
            except Exception as e:
                print(f"An error occurred: {e}")
                del self.clients[client]  # Remove the client from the dictionary
                client.close()
                break

    def receive(self):
        while True:
            client, address = self.server.accept()
            self.clients[client] = {'user_email': None, 'channel_id': 1}  # Add the client with their email and channel

            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()
    def broadcast(self, message, user, channel_id, date):
        for client, client_info in self.clients.items():
            if client_info['channel_id'] == channel_id:
                client.send(f' {date.strftime("%Y-%m-%d %H:%M:%S")} - {user}: {message}'.encode('utf-8'))
        
if __name__ == "__main__":
    my_server = Server()
    my_server.receive()