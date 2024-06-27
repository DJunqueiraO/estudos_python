import smtplib

sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "123"
subject = "Python is beautiful!"
body = "Python is delicious! Like a pie!"

message = f"""From: {sender}
to: {receiver}
subject: {subject}
{body}"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try: 
    server.login(sender, password)
    server.sendmail(sender, receiver, message)

    print('Email sent!')
except smtplib.SMTPAuthenticationError:
    print('Wrong password!')
