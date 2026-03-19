from generator import vytvor_fakturu


klient_a = {
	"meno": "Peter",
	"email": "peter@gmail.com",
	"suma": 500
}

klient_b = {
	"meno": "Jana",
	"email": "jana@gmail.com",
	"suma": 200
}

klient_c = {
	"meno": "Mira",
	"email": "mira@gmail.com",
	"suma": 350
}

klienti = [klient_a,klient_b,klient_c]
for klient in klienti:
	vytvor_fakturu(klient['meno'], klient['email'], klient['suma'])
