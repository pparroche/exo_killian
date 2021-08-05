from abc import ABC
import mysql.connector

class DB(ABC):
    conn = mysql.connector.connect(
        host='db',
        user='root',
        password='root',
        database='mabdd',
        port='3306',
        auth_plugin='mysql_native_password'
    )
# commit automatique qd une requête est faite en bdd
    #conn.autocommit = False

    @staticmethod
    def connect():
        try:
            cursor = DB.conn.cursor(dictionary = True)
            return cursor
        except mysql.connector.Error as e:
            print(e)