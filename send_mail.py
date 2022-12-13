import smtplib, ssl
import os
from dotenv import load_dotenv

load_dotenv()

def send_mail(message):
  host = "smtp.gmail.com"
  port = 465

  username="durlavk98@gmail.com"
  password=os.getenv('EMAIL_APP_PASSWORD')

  receiver = "durlavk98@gmail.com"
  context = ssl.create_default_context()

  # message = """\
  # Subject: Hi!
  # This is an automated mail.
  # """

  with smtplib.SMTP_SSL(host, port, context = context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)