import smtplib
from email.message import EmailMessage

msg = EmailMessage()

msg["From"] = "A well wisher :)"
msg["To"] = "tests.python.1908@gmail.com"
msg["Subject"] = "SUBSCRIBE"

msg.set_content("If you are watching this right now, please subscribe :)")

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login("geniouschartist@gmail.com", "egkxbyxyljhadvdz")
server.send_message(msg)

server.quit()