class Channel:
    def __init__(self, database):
        self.database = database

    def get_channel_id(self, channel_name):
        """
        Récupère l'identifiant d'un canal.
        """
        query = "SELECT id FROM channels WHERE name = %s"
        params = (channel_name,)
        return self.database.query(query, params)