import mysql.connector
class Database:
    def __init__(self):
        self.conn = self.connect_to_database()

    def connect_to_databse(self):
        """
        Établit une connexion à la base de données MySQL et retourne l'objet de connexion.
        """
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="myDiscord"
            )
            print("Connexion à la base de données réussie.")
            return conn
        except mysql.connector.Error as e:
            print(f"Erreur lors de la connexion à la base de données : {e}")
            return None

    def query(self, query, params=None):
        """
        Exécute une requête SQL avec des paramètres optionnels et renvoie les résultats.
        """
        results = []
        if self.conn:
            try:
                cursor = self.conn.cursor(dictionary=True)
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                results = cursor.fetchall()
                cursor.close()
            except mysql.connector.Error as e:
                print(f"Erreur lors de l'exécution de la requête SQL : {e}")
        return results

    def execute(self, query, params=None):
        """
        Exécute une requête SQL avec des paramètres optionnels.
        """
        if self.conn:
            try:
                cursor = self.conn.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                self.conn.commit()
                cursor.close()
            except mysql.connector.Error as e:
                print(f"Erreur lors de l'exécution de la requête SQL : {e}")

    def fermer_connexion(self):
        """
        Ferme la connexion à la base de données.
        """
        if self.conn:
            self.conn.close()
            print("Connexion à la base de données fermée.")
