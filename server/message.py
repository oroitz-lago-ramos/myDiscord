from server import Database

class Message(Database):
    def send_message(self, message_content, time, user_id, channel_id):
        """
        Crée un nouveau message dans la base de données.
        """
        query = "INSERT INTO message (message_content, time, user_id, channel_id) VALUES (%s, %s, %s, %s)"
        params = (message_content, time, user_id, channel_id)
        print("Trying to send message")
        self.execute(query, params)

    def load_messages_from_channel(self, channel_id):
        """
        Récupère les messages et les noms d'utilisateur des auteurs à partir d'un canal.
        """
        query = """
        SELECT m.message_content, u.name
        FROM message AS m
        JOIN user AS u ON m.user_id = u.ID
        WHERE m.channel_id = %s
        """
        params = (channel_id,)
        try:
            results = self.query(query, params)
            messages = []
            for row in results:
                message = {
                    'content': row[0],
                    'user_name': row[1]
                }
                messages.append(message)
            return messages
        except Exception as e:
            print(f"Erreur lors du chargement des messages du canal : {e}")
            return []
