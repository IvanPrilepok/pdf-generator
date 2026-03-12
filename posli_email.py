import smtplib

GMAIL = "prilepokivko@gmail.com"
HESLO = "wshs ggzl zffo azlo"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(GMAIL, HESLO)
print("Prihlásený")
server.quit()