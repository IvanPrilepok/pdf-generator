from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import date, timedelta
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from config import FONT_NAME, FONT_PATH, PAYMENT_DUE_DAYS
from utils import get_invoice_number, save_invoice_number, calculate_total
import qrcode
import os

pdfmetrics.registerFont(TTFont(FONT_NAME, FONT_PATH))

def generate_invoice(seller, client, items):
	number = get_invoice_number()
	
	today = date.today()
	due_date = date.today() + timedelta(days=PAYMENT_DUE_DAYS)

	pdf = canvas.Canvas(f"invoice_{seller['name']}_{number}.pdf")
	sirka = A4[0]
	vyska = A4[1]

	pdf.setFillColorRGB(0.95, 0.95, 0.95)
	pdf.rect(30, vyska - 150, sirka - 60, 70, fill=1, stroke=0)
	pdf.setFillColorRGB(0, 0, 0)
	pdf.setFont(FONT_NAME, 22)
	pdf.drawString(45, vyska - 110, f"INVOICE")
	pdf.setFont(FONT_NAME, 10)
	pdf.drawString(sirka - 100, vyska - 100, f"No. {number}")
	pdf.drawString(45, vyska - 135, f"Date: {today}")
	pdf.drawString(sirka - 200, vyska - 135, f"Due: {due_date}")
	
	pdf.setFont(FONT_NAME, 10)
	pdf.drawString(45, vyska - 175, f"SELLER:")
	pdf.setFont(FONT_NAME, 9)
	pdf.drawString(45, vyska - 190, f"{seller['name']} ")
	pdf.drawString(45, vyska - 205, f"{seller['email']} ")
	pdf.drawString(45, vyska - 220, f"{seller['iban']} ")

	pdf.setFont(FONT_NAME, 10)
	pdf.drawString(sirka/2, vyska - 175, f"CLIENT:")
	pdf.setFont(FONT_NAME, 9)
	pdf.drawString(sirka/2, vyska - 190, f"{client['name']} ")
	pdf.drawString(sirka/2, vyska - 205, f"{client['email']} ")

	data = [["Description", "Qty", "Unit Price", "Total"]] + [
    [item[0], item[1], f"{item[2]} EUR", f"{item[1] * item[2]} EUR"]
    for item in items
	]
	table = Table(data, colWidths=[270, 50, 90, 90])
	table.setStyle(TableStyle([
		("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
		("TEXTCOLOR", (0,0), (-1,0), colors.black),
		("GRID", (0,0), (-1,-1), 0.5, colors.grey)
	]))

	table.wrapOn(pdf, sirka, vyska)
	table.drawOn(pdf, 30, vyska - 350)	

	total = calculate_total(items)

	pdf.setFont(FONT_NAME, 11)
	pdf.drawString(380, vyska - 470, f"TOTAL: {total} EUR")

	pdf.setFont(FONT_NAME, 9)
	pdf.drawString(45, vyska - 525, "Thank you for your business.")

	qr_data = f"BCD\n001\n1\nSCT\n{seller['iban']}\n{seller['name']}\nEUR{total}"
	qr = qrcode.make(qr_data)
	qr.save("qr_temp.png")
	pdf.drawImage("qr_temp.png", sirka - 130, vyska - 560, width=80, height=80)
	os.remove("qr_temp.png")


	pdf.save()
	save_invoice_number(number + 1)





