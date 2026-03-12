from generator import vytvor_fakturu
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import date

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
