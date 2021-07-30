import smtplib  # mail transfer protocol
from email.message import EmailMessage
from string import Template  # substitute variables inside of text
from pathlib import Path  # ~= os.path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'name'
email['to'] = 'email address of receiver'
email['subject'] = 'enter subject'

email.set_content(html.substitute({'name': 'entername'}), 'html')

with smtplib.SMTP(host='enter host name her and port in port', port='') as smtp:
    smtp.ehlo()  # startup
    smtp.starttls()  # encryption
    smtp.login('<enter email address>', '<enter password>')
    smtp.send_message(email)
    print('All good boss!')
