from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import date, timedelta
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

pdfmetrics.registerFont(TTFont("DejaVu", "DejaVuSans.ttf"))

dnes = date.today()
splatnost = dnes + timedelta(days=7)

def vytvor_fakturu(meno, email, zoznam, klient, email_klienta, iban):
	cislo = cislo_faktury()
	celkom = celkova_suma(zoznam)
	pdf = canvas.Canvas(f"Faktúra_{meno}_{cislo}.pdf", pagesize=A4)
	sirka = A4[0]
	vyska = A4[1]

	pdf.setFillColorRGB(0.95, 0.95, 0.95)
	pdf.rect(35, vyska - 150, sirka - 70, 70, fill=1, stroke=0)
	pdf.setFillColorRGB(0, 0, 0)
	pdf.setFont("DejaVu", 16)
	pdf.drawString(45, vyska - 110, f"FAKTÚRA")
	pdf.setFont("DejaVu", 8)
	pdf.drawString(500, vyska - 100, f"č.{cislo}")
	pdf.setFont("DejaVu", 12)
	pdf.drawString(45, vyska - 135, f"Dátum: {dnes}")
	pdf.drawString(412, vyska - 135, f"Splatnosť: {splatnost}")

	data = [["Popis", "Ks", "Suma"]] + zoznam
	tabulka = Table(data, colWidths=[300, 50, 100])
	tabulka.setStyle(TableStyle([
		("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
		("TEXTCOLOR", (0,0), (-1,0), colors.black),
		("GRID", (0,0), (-1,-1), 0.5, colors.grey)
	]))
	tabulka.wrapOn(pdf, sirka, vyska)
	tabulka.drawOn(pdf, 70, vyska - 350)
	
	pdf.setFont("DejaVu", 10)
	pdf.drawString(80, vyska - 200, f"PREDÁVAJÚCI:")
	pdf.drawString(80, vyska - 220, f"{meno}")
	pdf.drawString(80, vyska - 240, f"{email}")
	pdf.drawString(300, vyska - 200, f"ODBERATEĽ:")
	pdf.drawString(300, vyska - 220, f"{klient}")
	pdf.drawString(300, vyska - 240, f"{email_klienta}")

	pdf.setFont("DejaVu", 12)
	pdf.drawString(60, vyska - 400, f"CELKOM: {celkom} EUR")
	pdf.drawString(335, vyska - 400, f"IBAN: {iban}")
	pdf.drawString(230, vyska - 460, f"Ďakujeme za spoluprácu.")		
	
	
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

def celkova_suma(zoznam):
	celkom = sum(p[1] * p[2] for p in zoznam)
	return celkom
