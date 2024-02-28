import socket
import json

class Client:
    def __init__(self, host='127.0.0.1', port=55555):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

    def send_message(self, message):
        self.client.send(message.encode('ascii'))
    def receive_message(self):
        try:
            message = self.client.recv(20000).decode('ascii')
            return message
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    def receive_loop_message(self):
        try:
            self.client.settimeout(2)  # Set a timeout of 1 second for receiving messages
            message = self.client.recv(8000).decode('ascii')
            return message
        except socket.timeout:
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def switch_channel(self, channel_id):
        self.send_message(f'switch_channel > {channel_id}')

    def send_chat_message(self, user, message):
        self.send_message(f'message > {message}')
    
    def load_messages(self):
        self.send_message('load_messages')
        messages_str = self.receive_message()
        if messages_str:
            messages = json.loads(messages_str)
        else:
            messages = []
        return messages

    def load_channels(self):
        self.send_message('load_channels')
        channels_str = self.receive_message()
        if channels_str:
            channels = json.loads(channels_str)
        else:
            channels = []
        return channels