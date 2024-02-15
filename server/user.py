class User:
    def __init__(self, email, password, database):
        self.email = email
        self.password = password
        self.databse = database
    def create(self, lastname, name):
        """
        Crée un nouvel utilisateur dans la base de données.
        """
        query = "INSERT INTO users (lastname, name, email, password, role_id) VALUES (%s, %s)"
        params = (lastname, name, self.email, self.password, 2)
        self.database.execute(query, params)
    def delete(self):
        """
        Supprime l'utilisateur de la base de données.
        """
        query = "DELETE FROM users WHERE email = %s"
        params = (self.email,)
        self.database.execute(query, params)
    
    
    
    