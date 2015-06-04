#!/usr/bin/env python3
#
# Created by Nanohard
#
# This script uses xidletime to calculate how long
# you've been away from the computer. After a specified
# amount of time it will send an email.
#

import subprocess
from time import sleep
import smtplib
from email.mime.text import MIMEText
import sys

while True:
    output = subprocess.check_output(['xprintidle']) # xprintidle prints time in milliseconds
    output = int(output.decode())

    if output > 600000000: # about 7 days

        with open('/full/path/to/file') as fp:
            # Create a text/plain message
            file1 = MIMEText(fp.read())

        HOST = "mail.example.com"   # mail server SMTP address
        PORT = "587"                # mail server SMTP port
        SUBJECT = "Time-bomb activated"
        TO = "someone@example.com"
        FROM = "me@example.com"
        text = str.join("\n", (
                "Something happened to me, so here's the info I told you about:",
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
            server.login('me@example.com', 'password')
            server.sendmail(FROM, [TO], BODY)
            server.quit()
            print("Success! Email sent.")   # uncomment for testing
        except IOError as e:
            print("IOError:", e, e.args)
            sys.exit(1)
        else:
            sys.exit(1)

    sleep(600)  # check idle time every 10 minutes
