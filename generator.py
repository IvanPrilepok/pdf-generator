from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import date

today = date.today()

def vytvor_fakturu(meno, email, suma):
	pdf = canvas.Canvas(f"faktura_{meno}.pdf", pagesize=A4)
	sirka, vyska = A4
	pdf.setFont("Helvetica", 24)
	pdf.drawString(50, vyska - 80, "FAKTÚRA c. 001")

	pdf.setFont("Helvetica", 12)
	pdf.drawString(50, vyska - 130, f"Predávajúci: {meno}")
	pdf.drawString(50, vyska - 150, f"Email: {email}")

	pdf.drawString(50, vyska - 220, "Popis služby")
	pdf.drawString(350, vyska - 220, "Suma")

	pdf.drawString(50, vyska - 250, "Python automatizácia")
	pdf.drawString(350, vyska - 250, f"{suma} EUR")

	pdf.drawString(50, vyska - 170, f"Dátum: {today}")

	pdf.setFont("Helvetica-Bold", 14)
	pdf.drawString(50, vyska - 320, f"CELKOM: {suma} EUR")
	pdf.save()

vytvor_fakturu("Peter", "peter@gmail.com", 500)
vytvor_fakturu("Jana", "jana@gmail.com", 200)
vytvor_fakturu("Mira", "mira@gmail.com", 330)