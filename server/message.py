class Message:
    def __init__(self, database):
        self.database = database
    def create(self, message_content, time, user_id, channel_id):
        """
        Crée un nouveau message dans la base de données.
        """
        query = "INSERT INTO message (message_content, time, user_id, channel_id) VALUES (%s, %s, %s)"
        params = (message_content, time, user_id, channel_id)
        self.database.execute(query, params)
    def load_messages_from_channel(self, channel_id):
        """
        Récupère les messages d'un canal.
        """
        query = "SELECT * FROM message WHERE channel_id = %s"
        params = (channel_id,)
        results = self.database.query(query, params)
        messages = []
        for row in results:
            messages.append(row[1])
        return messages