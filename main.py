import pandas as pd 
from generator import vytvor_fakturu

def rucne_zadanie():
	zoznam = []
	meno = input("Zadajte Vaše meno: ")
	email = input("Zadajte Váš email: ")
	iban = input("Zadajte Váš IBAN: ")
	klient = input("Zadajte meno klienta: ")
	email_klienta = input("Zadajte email klienta: ")
	while True:
		popis = input("Zadajte popis položky (alebo Enter pre koniec): ")
		if popis == "":
			print("Končím...")
			break
		ks = int(input("Zadajte počet ks: "))
		suma = int(input("Zadajte sumu: "))
		zoznam.append([popis, ks, suma])
	return vytvor_fakturu(meno, email, zoznam, klient, email_klienta, iban)

def zo_suboru():
	meno = input("Zadajte Vaše meno: ")
	email = input("Zadajte Váš email: ")
	iban = input("Zadajte Váš IBAN: ")
	klient = input("Zadajte meno klienta: ")
	email_klienta = input("Zadajte email klienta: ")
	cesta = input("Zadajte cestu k súboru (.xlsx alebo .csv): ")
	df = pd.read_excel(cesta)
	zoznam = df[['popis', 'ks', 'suma']].values.tolist() 
	return vytvor_fakturu(meno, email, zoznam, klient, email_klienta, iban)

while True:
	try:
		print("\n---VYTVOR FAKTÚRU---")
		print("1. Ručné zadanie")
		print("2. Excel/CSV")
		print("3. Koniec")

		volba = input("\nZadajte možnosť: ")

		if volba == "1":
			rucne_zadanie()
		elif volba == "2":
			zo_suboru()
		elif volba == "3":
			print("Končím...")
			break
		else:
			print("Neplatná možnosť.")

	except ValueError:
		print("Nesprávne údaje.")

	except Exception as e:
		print(f"{e}")	