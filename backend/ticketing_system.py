# ticketing_system.py
import sqlite3
import hashlib
import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


DB_PATH = 'db/ticketing.db'

def create_ticket(user_id, issue):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO tickets (user_id, issue) VALUES (?, ?)", (user_id, issue))
    
    conn.commit()
    conn.close()

def get_open_tickets():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tickets WHERE status='Open'")
    tickets = cursor.fetchall()

    conn.close()
    return tickets

def register_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Generate a secure salt for password hashing
    salt = secrets.token_hex(16)

    # Hash the password with the salt using SHA-256
    password_hash = hashlib.sha256((password + salt).encode()).hexdigest()

    cursor.execute("INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)", (username, password_hash, salt))
    
    conn.commit()
    conn.close()

def authenticate_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()

    if user:
        stored_password_hash = user[2]  # Assuming password_hash is in the third column
        stored_salt = user[3]  # Assuming salt is in the fourth column

        # Hash the input password with the stored salt
        input_password_hash = hashlib.sha256((password + stored_salt).encode()).hexdigest()

        # Compare the stored password hash with the newly hashed input password
        if stored_password_hash == input_password_hash:
            conn.close()
            return user

    conn.close()
    return None
