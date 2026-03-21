from generator import vytvor_fakturu

while True:
	try:
		print("\n---FAKTURAČNÝ SYSTÉM---")
		print("1. Vygeneruj faktúru")
		print("2. Koniec")
		
		volba = input("Zadajte možnosť: ")

		if volba == "1":
			zoznam = []
			meno = input("Zadajte meno: ")
			email = input("Zadajte email: ")
			while True:
				popis = input("Zadajte popis položky (alebo Enter pre koniec): ")
				if popis == "":
					print("Končím...")
					break
				suma = int(input("Zadajte sumu: "))
				zoznam.append({"popis": popis, "suma": suma})
			vytvor_fakturu(meno, email, zoznam)
			
		elif volba == "2":
			print("Končím...")
			break
		
		else:
			print("Zadajte možnosť 1 alebo možnosť 2.")

	except ValueError:
		print("Nesprávne údaje.")
		pass
	
	except Exception as e:
		print(f"{e}")
	