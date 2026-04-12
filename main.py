import pandas as pd 
from generator import generate_invoice
from database import init_db, add_client, get_clients, get_client_by_id
from config import DEFAULT_SELLER_ID

def select_client():
	clients = get_clients()

	if not clients:
		print("No clients found.")
		return None

	for i, c in enumerate(clients, 1):
		print(f"{i}. {c[1]} ({c[2]})")

	choice = int(input("Select client number: ")) - 1
	selected = clients[choice]

	return {'name': selected[1], 'email': selected[2], 'iban': selected[3]}

def add_new_client():
	name = input("Add name: ")
	email = input("Add email: ")
	iban = input("Add IBAN: ")
	add_client(name, email, iban)
	print(f"Client {name} added successfully.")

def manual_invoice():
	seller_data = get_client_by_id(DEFAULT_SELLER_ID)
	seller = {"name": seller_data[1], "email": seller_data[2], "iban": seller_data[3]}

	print("Select client: ")
	client = select_client()
	if not client:
		return

	items = []
	while True:
		try:
			description = input("Item description (Enter to finish): ")
			if description == "":
				break
			qty = int(input("Quantity: "))
			price = float(input("Unit price: "))
			items.append([description, qty, price])
		except ValueError:
			print("Invalid input, try again")
			continue

	generate_invoice(seller, client, items)
	print("Invoice generated successfully.")

def excel_invoice():
	seller_data = get_client_by_id(DEFAULT_SELLER_ID)
	seller = {"name": seller_data[1], "email": seller_data[2], "iban": seller_data[3]}

	print("Select client: ")
	client = select_client()
	if not client:
		return

	path = input("Enter file path (.xlsx or .csv): ")
	if path.endswith(".xlsx"):
		df = pd.read_excel(path, engine="openpyxl")
	else:
		df = pd.read_csv(path)
	items = df[['description', 'qty', 'price']].values.tolist()
	generate_invoice(seller, client, items)
	print("Invoice generated successfully.")

def main():
	init_db()
	while True:
		print("\n---GENERATE INVOICE---")
		print("1 - Add client")
		print("2 - Manual invoice")
		print("3 - Excel invoice")
		print("4 - End")

		choice = input("\nSelect a choice(1, 2, 3 or 4): ")

		if choice == "1":
			add_new_client()
		elif choice == "2":
			manual_invoice()
		elif choice == "3":
			excel_invoice()
		elif choice == "4":
			print("Ending...")
			break
		else:
			print("Invalid choice")
			continue

if __name__ == "__main__":
	main()