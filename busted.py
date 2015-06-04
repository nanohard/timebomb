import subprocess
from time import sleep
import smtplib
from email.mime.text import MIMEText
import string
import sys

while True:
    output = subprocess.check_output(['xprintidle']) # xprintidle prints time in milliseconds
    output = int(output.decode())

    if output > 600000000: # about 7 days

        with open('/home/user/Desktop/user') as fp:
            # Create a text/plain message
            file1 = MIMEText(fp.read())

        HOST = "mail.posignite.com"
        PORT = "587"
        SUBJECT = "Shit went south"
        TO = "nick@posignite.com"
        FROM = "william@posignite.com"
        text = str.join("\n", (
                "Things went sideways, so here's my creds for everything, including my VPS and home computer SSH (LOCAL). ctrl+f is your friend:",
                "%s" %file1
                ))
        BODY = str.join("\n", (
                "From: %s" % FROM,
                "To: %s" % TO,
                "Subject: %s" % SUBJECT ,
                "",
                text
                ))
        try:
            server = smtplib.SMTP(HOST, PORT)
            server.ehlo()
            server.starttls()
            server.login('william@posignite.com', 'Ie7qeEagxoDnhpiIZ')
            server.sendmail(FROM, [TO], BODY)
            server.quit()
            print("Busted sent...")
        except IOError as e:
            print("IOError:", e, e.args)
            sys.exit(1)
        else:
            sys.exit(1)

    sleep(600)
