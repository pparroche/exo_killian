from model.db import DB


class QueriesMaBdd():
    def __init__(self):
        self.conn = DB.connect()

    def fetch_all_users(self):
        self.conn.execute(
            """ SELECT * from utilisateurs
            """
        )
        rows = self.conn.fetchall()
        return rows
    
    def add_user(self, utilis):
        self.conn.execute(
            f"""
            INSERT INTO utilisateurs (id_utilisateur, nom, prenom) VALUES ({utilis.get('id')}, {utilis.get('nom')}, , {utilis.get('prenom')})
            """
        )