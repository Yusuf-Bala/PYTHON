#go to email and enable 2fa
#generate app password
#create a function to send mail

from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'hackbabz69@gmail.com'
email_password = 'rqdtpevoyhzpbtqv'
email_receiver = 'liwila6094@cohodl.com'

subject = "new subscriber"
body = """
this is a message to you
"""

em = EmailMessage()
em['FROM'] = email_sender
em['TO'] = email_receiver
em['SUBJECT'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.email.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
