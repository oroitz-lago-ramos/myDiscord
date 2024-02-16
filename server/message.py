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
            results = self.database.query(query, params)
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

        
    # def get_message_user_name(self, message_id):
    #     """
    #     Récupère l'utilisateur d'un message.
    #     """
    #     query = """
    #     SELECT u.name
    #     FROM message AS m
    #     JOIN user AS u ON m.user_id = u.id
    #     WHERE m.id = %s
    #     """
    #     params = (message_id,)
    #     result = self.database.query(query, params)
    #     return result[0][0] if result else None
