from triedy import Klient

klienti = [Klient("Peter", "p@g.com", 500), Klient("Jana", "j@g.com", 200)]

def spocitaj_faktury(klienti):
	celkom = 0
	for klient in klienti:
		celkom = celkom + klient.suma
	return celkom
print(spocitaj_faktury(klienti))	