from server import Database

class User(Database):
    def __init__(self):
        super().__init__()
        self.user_email = "oroitz@gmail.com"
        self.user_password = "root"
        self.user_auth = False

    def create(self, lastname, name, password, email, role_id):
        """
        Crée un nouvel utilisateur dans la base de données.
        """
        query = "INSERT INTO user (lastname, name, email, password, role_id) VALUES (%s, %s)"
        params = (lastname, name, email, password, 3)
        self.execute(query, params)

    def delete(self, email):
        """
        Supprime l'utilisateur de la base de données.
        """
        query = "DELETE FROM user WHERE email = %s"
        params = (email,)
        self.execute(query, params)

    def select_user(self, email, password):
        """
        Sélectionne un utilisateur dans la base de données.
        """
        query = "SELECT ID FROM user WHERE email = %s AND password = %s"
        params = (email, password)
        try:
            result = self.query(query, params)
            if result:  
                return result[0][0]  
            else:
                return None  
        except Exception as e:
            print(f"Erreur lors de la sélection de l'utilisateur : {e}")
            return None

    def get_user_name(self, user_id):
        """
        Récupère le nom d'un utilisateur.
        """
        query = "SELECT name FROM user WHERE ID = %s"
        params = (user_id,)
        result = self.query(query, params)
        return result[0][0] if result else None

    def set_user_role(self, role_name):
        """
        Définit le rôle de l'utilisateur.
        """
        query = "UPDATE user SET role_id = %s WHERE email = %s"
        params = (role_name, self.email)
        self.execute(query, params)

    def get_user_role(self):
        """
        Récupère le rôle de l'utilisateur.
        """
        query = "SELECT role_id FROM user WHERE email = %s"
        params = (self.email,)
        result = self.query(query, params)
        return result[0][0] if result else None

    def get_user_id(self):
        """
        Récupère l'identifiant de l'utilisateur.
        """
        query = "SELECT ID FROM user WHERE email = %s"
        params = (self.email,)
        result = self.query(query, params)
        return result[0][0] if result else None

    def set_user(self,email, password):
        self.user_email = email
        self.user_password = password
