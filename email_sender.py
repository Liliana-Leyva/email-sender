import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from']='your name'
email['to']= 'email@gmail.com'
email['subject'] = 'trying this email app'

email.set_content(html.substitute({'name': 'tin tin'}),'html')

with smtplib.SMTP(host ='smtp.gmail.com', port =587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sendersemail@gmail.com', 'generatedPass')
    smtp.send_message(email)
    print('all good boss!')