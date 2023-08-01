import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from']='your name'
email['to']= 'myemail@gmail.com'
email['subject'] = 'trying this email app'

email.set_content('I am learning Python')

with smtplib.SMTP(host ='smtp.gmail.com', port =587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('mygmailemail', 'generatedpassword')
    smtp.send_message(email)
    print('all good boss!')