class Message:
    def __init__(self, database):
        self.database = database
    def create(self, message_content, time, user_id, channel_id):
        """
        Crée un nouveau message dans la base de données.
        """
        query = "INSERT INTO messages (message_content, time, user_id, channel_id) VALUES (%s, %s, %s)"
        params = (message_content, time, user_id, channel_id)
        self.database.execute(query, params)
    def load_messages_from_channel(self, channel_id):
        """
        Récupère les messages d'un canal.
        """
        query = "SELECT * FROM messages WHERE channel_id = %s"
        params = (channel_id,)
        return self.database.query(query, params)