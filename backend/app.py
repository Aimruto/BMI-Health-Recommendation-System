from flask import Flask, request, jsonify
import sqlite3
import re
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)


def initialize_database():
    conn = sqlite3.connect('users.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  fullname TEXT NOT NULL,
                  email TEXT NOT NULL UNIQUE,
                  username TEXT NOT NULL UNIQUE,
                  password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def is_valid_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+(\.[\w]+)+$', email)


def is_valid_password(password):
    return len(password) >= 6

@app.route('/api/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.json
        fullname = data.get('fullname')
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')
        print(data)
        
        if not all([fullname, email, username, password]):
            return jsonify({'error': 'All fields are required'}), 400
        
        if not is_valid_email(email):
            return jsonify({'error': 'Invalid email format'}), 400
        
        if not is_valid_password(password):
            return jsonify({'error': 'Password must be at least 6 characters long'}), 400
        
        hashed_password = generate_password_hash(password)
        
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (fullname, email, username, password) VALUES (?, ?, ?, ?)", (fullname, email, username, hashed_password))
            conn.commit()
            conn.close()
            return jsonify({'message': 'User signed up successfully'}), 201
        except sqlite3.IntegrityError:
            conn.close()
            return jsonify({'error': 'Email or username already exists'}), 400
    else:
        return jsonify({'message': 'GET request received for signup'}), 200

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    if not all([email, password]):
        return jsonify({'error': 'Email and password are required'}), 400
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    
    if user and check_password_hash(user[4], password):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid email or password'}), 401

if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)
