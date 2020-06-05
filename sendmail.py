import os
import smtplib
from email.message import EmailMessage

def sendmail(subj):

    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER')) #if first part of address is the same as username in system
    subject = subject
    body = "Please check your system and resolve the issue as soon as possible."
    msg = EmailMessage()
    msg["From"] = sender
    msg["Subject"] = subject
    msg["To"] = receiver
    msg.set_content(body)
    
    # Attachments:
    # msg.add_attachment(open(message, "rb").read(), maintype="multypart", subtype="pdf", filename='processed.pdf')
    # msg.add_attachment(message, filename='/tmp/processed.pdf')
    
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()
