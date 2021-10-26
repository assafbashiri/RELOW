import smtplib, ssl


class emailHandler:
    def __init__(self):
        self.x =1

    def sendemail(self, receiver_email, message):
        port = 587  # For starttls
        return False
        smtp_server = "smtp.gmail.com"
        sender_email = "shareit1256@gmail.com"
        password = "bolo1995"
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
