from flask import Flask, request, jsonify, Response
import json
import mysql.connector
from werkzeug.utils import redirect
from flask.templating import render_template
from model.SQLQueries import QueriesMaBdd

app= Flask(__name__)


@app.route("/")
def hello():
    return render_template('bonjour.html')

@app.route('/all_users', methods=['GET'])
def all_users():
    result = QueriesMaBdd().fetch_all_users()
    return render_template('GetUsers.html', data=result)

@app.route('/add_user_template/')
def add_user_template():
    return render_template('add_user.html')
    
@app.route('/insert_user/', methods=['POST', 'GET'])
def insert_user():
    data = request.form
    QueriesMaBdd().add_user(data)
    return redirect('http://localhost:5000')
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    