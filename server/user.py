from typing import Any


class User:
    def __init__(self, database):
        self.database = database
    def create(self, lastname, name, password, email, role_id):
        """
        Crée un nouvel utilisateur dans la base de données.
        """
        query = "INSERT INTO user (lastname, name, email, password, role_id) VALUES (%s, %s)"
        params = (lastname, name, email, password, 3)
        self.database.execute(query, params)
    def delete(self, email: Any):
        """
        Supprime l'utilisateur de la base de données.
        """
        query = "DELETE FROM user WHERE email = %s"
        params = (email,)
        self.database.execute(query, params)
  
    
    def authenticate(self, email, password):
        """
        Authenticates a user based on their email and password.
        """
        query = "SELECT ID FROM user WHERE email = %s AND password = %s"
        params = (email, password)

        try:
            result = self.database.query(query, params)
            if result:
                return True  # Return True if a user with the given email and password exists
            else:
                return False  # Return False otherwise
        except Exception as e:
            print(f"Error authenticating user: {e}")
            return False  # Return False if an error occurred
    
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
    
    def get_user_name(self, user_id):
        """
        Récupère le nom d'un utilisateur.
        """
        query = "SELECT name FROM user WHERE ID = %s"
        params = (user_id,)
        result = self.database.query(query, params)
        return result[0][0] if result else None
    
    def set_user_role(self, role_name):
        """
        Définit le rôle de l'utilisateur.
        """
        query = "UPDATE user SET role_id = %s WHERE email = %s"
        params = (role_name, self.email)
        self.database.execute(query, params)
    
    def get_user_role(self):
        """
        Récupère le rôle de l'utilisateur.
        """
        query = "SELECT role_id FROM user WHERE email = %s"
        params = (self.email,)
        result = self.database.query(query, params)
        return result[0][0] if result else None
    
    def get_id(self, email):
        """
        Récupère l'identifiant de l'utilisateur.
        """
        query = "SELECT ID FROM user WHERE email = %s"
        params = (email,)
        result = self.database.query(query, params)
        return result[0][0] if result else None
    
    def set_user(self,email, password):
        self.user_email = email
        self.user_password = password