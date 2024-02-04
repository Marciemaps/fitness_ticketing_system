# backend/authentication.py
import hashlib

def hash_password(password):
    # Implement your password hashing logic here
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password
