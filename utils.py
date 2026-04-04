import sqlite3
from config import INVOICE_NUMBER_FILE

def get_invoice_number():
	try:
		with open(INVOICE_NUMBER_FILE, "r", encoding="utf-8") as f:
			return int(f.read())
	except FileNotFoundError:
		return 1

def save_invoice_number(number):
	with open(INVOICE_NUMBER_FILE, "w", encoding="utf-8") as f:
		f.write(str(number))

def calculate_total(items):
	return sum(item[1] * item[2] for item in items)