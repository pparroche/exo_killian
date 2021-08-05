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
            INSERT INTO utilisateurs (id_utilisateur, nom, prenom, id_adresse) VALUES({utilis.get('id_utilisateur')}, {utilis.get('nom')}', '{utilis.get('prenom')}','{utilis.get('id_adresse')}')
            """
        )