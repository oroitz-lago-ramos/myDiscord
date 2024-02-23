class Channel:
    def __init__(self, database):
        self.database = database

    def get_channel_id(self, channel_name):
        """
        Récupère l'identifiant d'un canal.
        """
        query = "SELECT id FROM channel WHERE channel_name = %s"
        params = (channel_name,)
        return self.database.query(query, params)
    def get_channel_name(self, channel_id):
        """
        Récupère le nom d'un canal.
        """
        query = "SELECT channel_name FROM channel WHERE id = %s"
        params = (channel_id,)
        return self.database.query(query, params)
    def get_channels(self):
        """
        Récupère tous les canaux.
        """
        query = "SELECT * FROM channel"
        return self.database.query(query)
       