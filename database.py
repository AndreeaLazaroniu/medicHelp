import sqlite3
import hashlib

def get_connection():
    conn = sqlite3.connect('database.db')
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Tabel Utilizatori
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            password TEXT,
            role TEXT
        )
    ''')
    
    # Tabel Diagnostice
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS diagnostics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            medic_id INTEGER,
            prediction TEXT,
            probability REAL,
            input_type TEXT, -- 'Tabular' sau 'Image'
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            medic_confirmation TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

# Inițializare bază de date
if __name__ == "__main__":
    create_tables()
    print("Baza de date a fost creată cu succes!")