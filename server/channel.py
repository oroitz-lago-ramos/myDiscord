from server import Database

class Channel(Database):
    def get_channel_id(self, channel_name):
        """
        Récupère l'identifiant d'un canal.
        """
        query = "SELECT id FROM channel WHERE channel_name = %s"
        params = (channel_name,)
        return self.query(query, params)

    def get_channel_name(self, channel_id):
        """
        Récupère le nom d'un canal.
        """
        query = "SELECT channel_name FROM channel WHERE id = %s"
        params = (channel_id,)
        return self.query(query, params)

    def get_channels(self):
        """
        Récupère tous les canaux.
        """
        query = "SELECT * FROM channel"
        result = self.query(query)
        names = []
        for row in result:
            names.append(row[1])
        return names
