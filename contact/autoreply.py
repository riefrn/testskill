import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def autoreply(toaddr):
	"""SEnd reply to contact submission."""

	fromaddr = "rief.rn@gmail.com"
	password = "******"
	msg = MIMEMultipart()

	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Contact Concert reply"

	body = "Thanks for contacting us. We will get back to you after processing your submission. Arief, CEO, Concert Django Project"

	msg.attach(MIMEText(body, 'plain'))

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, password)
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
