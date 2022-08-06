from fileinput import filename
import os
import ssl
import smtplib
import imghdr
from email.message import EmailMessage


sender_email = ''
password_email = ''

email_recipient = ''

subject = ''
body = """

"""

em = EmailMessage()
em['From'] = sender_email
em['To'] = email_recipient
em['Subject'] = subject
em.set_content(body)

#Attach Files 
with open('', 'rb') as file:
    file_data = file.read()
    file_type = imghdr.what(file.name)
    file_name = file.name
em.add_attachment(file_data, filename =  file_name, subtype = file_type, maintype='')

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender_email, password_email)
    smtp.sendmail(sender_email, email_recipient, em.as_string())
