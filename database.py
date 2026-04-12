import sqlite3
from config import DB_NAME

def init_db():
	conn = sqlite3.connect(DB_NAME)
	cursor = conn.cursor()

	cursor.execute("""
		CREATE TABLE IF NOT EXISTS clients (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			name TEXT NOT NULL,
			email TEXT NOT NULL,
			iban TEXT NOT NULL
		)
	""")

	conn.commit()
	conn.close()

def add_client(name, email, iban):
	conn = sqlite3.connect(DB_NAME)
	cursor = conn.cursor()

	cursor.execute(
		"INSERT INTO clients (name, email, iban) VALUES (?, ?, ?)",
		(name, email, iban)
	)		

	conn.commit()
	conn.close()

def get_clients():
	conn = sqlite3.connect(DB_NAME)
	cursor = conn.cursor()

	cursor.execute("SELECT * FROM clients")
	clients = cursor.fetchall()

	conn.close()
	return clients

def get_client_by_id(client_id):
	conn = sqlite3.connect(DB_NAME)
	cursor = conn.cursor()

	cursor.execute("SELECT * FROM clients WHERE id = ?", (client_id,))
	client = cursor.fetchone()

	conn.close()
	return client

