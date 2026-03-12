from triedy import Klient
from generator import vytvor_fakturu

klienti = []

while True:
	print("\n1. Pridaj klienta")
	print("2. Zobraz klientov")
	print("3. Vygeneruj faktúru")
	print("4. Koniec")

	volba = input("Vyber: ")

	if volba == "1":
		meno = input("Meno: ")
		email = input("Email: ")
		suma = int(input("Suma: "))
		klienti.append(Klient(meno,email,suma))
		pass
	elif volba == "2":
		for klient in klienti:
			print(klient)
		pass
	elif volba == "3":
		hladane_meno = input("Zadaj meno: ")
		for klient in klienti:
			if klient.meno == hladane_meno:
				klient.vytvor_fakturu()
		pass
	else:
		break

		
