from flask import Flask, request, jsonify, Response
import json
import mysql.connector


app= Flask(__name__)

def getMysqlConnection():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'mabdd'
    }
    return mysql.connector.connect(**config)

@app.route("/")
def hello():
    return "Hello world"

@app.route('/all_users', methods=['GET'])
def all_users(self):
    db = getMysqlConnection()
    try:
        users="SELECT nom, prenom from utilisateurs"
        cursor = db.cursor()
        cursor.execute(users)
        output_json = cursor.fetchall()
        return jsonify(results=output_json)
    except Exception as e:
        print("Error in SQL:\n", e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    