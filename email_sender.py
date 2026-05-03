import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from config import DEFAULT_SELLER_ID
from database import get_client_by_id
from dotenv import load_dotenv
import os

load_dotenv()
password = os.getenv("EMAIL_PASSWORD")

def send_invoice(to_email, pdf_path):
    seller_data = get_client_by_id(DEFAULT_SELLER_ID)
    from_email = seller_data[2]

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = "Invoice"

    msg.attach(MIMEText("Please find your invoice attached.", "plain"))

    with open(pdf_path, "rb") as f:
        attachment = MIMEBase("application", "octet-stream")
        attachment.set_payload(f.read())
        encoders.encode_base64(attachment)
        attachment.add_header("Content-Disposition", f"attachment; filename={pdf_path}")
        msg.attach(attachment)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())

    print(f"Invoice sent to {to_email}")

if __name__ == "__main__":
    send_invoice("prilepokivko@gmail.com", "invoice_Ivan Prilepok_6.pdf")