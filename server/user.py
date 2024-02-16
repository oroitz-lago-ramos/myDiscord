from typing import Any


class User:
    def __init__(self, email, password, database):
        self.email = email
        self.password = password
        self.database = database
        self.authentified_user = None
    def create(self, lastname, name):
        """
        Crée un nouvel utilisateur dans la base de données.
        """
        query = "INSERT INTO user (lastname, name, email, password, role_id) VALUES (%s, %s)"
        params = (lastname, name, self.email, self.password, 3)
        self.database.execute(query, params)
    def delete(self):
        """
        Supprime l'utilisateur de la base de données.
        """
        query = "DELETE FROM user WHERE email = %s"
        params = (self.email,)
        self.database.execute(query, params)
  
    
    
    def select_user(self, email, password):
        """
        Sélectionne un utilisateur dans la base de données.
        """
        query = "SELECT ID FROM user WHERE email = %s AND password = %s"
        params = (email, password)
        try:
            result = self.database.query(query, params)
            if result:  # Vérifie si la requête a renvoyé des résultats
                return result[0][0]  # Retourne l'ID de l'utilisateur s'il existe
            else:
                return None  # Retourne None si aucun utilisateur correspondant n'a été trouvé
        except Exception as e:
            print(f"Erreur lors de la sélection de l'utilisateur : {e}")
            return None