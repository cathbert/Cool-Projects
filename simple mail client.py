import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# -> https://www.google.com/settings/security/lesssecureapps
server = smtplib.SMTP('smtp.gmail.com', 25)
server.ehlo()
server.starttls()
server.ehlo()

email = "" # -> Sender email here
pwd = "" # -> Sender passworrd here
try:
    server.login(email, pwd)
except smtplib.SMTPAuthenticationError as ae:
    print("Authentication Error!")

msg = MIMEMultipart()
msg['From'] = "GoofyCoder"
msg['To'] = "cmutaurwa@gmail.com"
msg['Subject'] = "Testing one two"

# -> Adding text from file
with open('message.txt', 'r') as f:
    message = f.read()
    msg.attach(MIMEText(message, 'plain'))

# -> Adding an attachment
filename = "goofy_logo.jpg"
attachment = open(filename, 'rb')

pay_load = MIMEBase('Application', 'octet-stream')
pay_load.set_payload(attachment.read())

encoders.encode_base64(pay_load)
pay_load.add_header("Content-Disposition", f"attachment; filename={filename}")
msg.attach(pay_load)

text = msg.as_string()
try:
    server.sendmail('goofycoder.cch@gmail.com', 'cmutaurwa@gmail.com', text)
    print("Message sent!")
except smtplib.SMTPSenderRefused as sre:
    print("Sender refused!")
except smtplib.SMTPRecipientsRefused as rre:
    print("Recipient Refused!")
except smtplib.SMTPConnectError as ce:
    print("Failed to connect!")