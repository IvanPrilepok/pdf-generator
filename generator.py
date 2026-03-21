from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import date
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont 

pdfmetrics.registerFont(TTFont("DejaVu", "DejaVuSans.ttf"))

today = date.today()

def vytvor_fakturu(meno, email, zoznam):
	cislo = cislo_faktury()
	pdf = canvas.Canvas(f"faktura_{meno}_{cislo}.pdf", pagesize=A4)
	sirka, vyska = A4
	pdf.setFont("DejaVu", 24)
	pdf.drawString(50, vyska - 80, f"FAKTÚRA č.{cislo}")

	pdf.setFont("DejaVu", 12)
	pdf.drawString(50, vyska - 130, f"Predávajúci: {meno}")
	pdf.drawString(50, vyska - 150, f"Email: {email}")

	y = vyska - 220
	celkova_suma = 0
	for p in zoznam:
		popis = p['popis']
		suma = p['suma']
		pdf.drawString(50, y, popis)
		pdf.drawString(350, y, f"{suma} EUR")
		celkova_suma += suma
		y -= 20

	pdf.drawString(50, vyska - 170, f"Dátum: {today}")

	pdf.setFont("DejaVu", 14)
	pdf.drawString(50, vyska - 320, f"CELKOM: {celkova_suma} EUR")
	pdf.save()
	uloz_cislo_faktury(cislo + 1)
	
def cislo_faktury():
	try:
		with open("cislo_faktury.txt", "r", encoding="utf-8") as subor:
			cislo = int(subor.read())
		return cislo 
	except:
		return 1
def uloz_cislo_faktury(cislo):
	with open("cislo_faktury.txt", "w", encoding="utf-8") as subor:
		subor.write(str(cislo))

