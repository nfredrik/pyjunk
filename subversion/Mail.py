import smtplib
import email.utils
from email.mime.text import MIMEText
import getpass

class Mail(object):

    def __init__(self, to, username, password, servername):
        self.to_email = to
        self.username = username
        self.password = password
        self.server = smtplib.SMTP(servername)

    def send(self, mesg):
        # Create message 
        msg = MIMEText('be careful')
        msg.set_unixfrom('configuration management')
        msg['To'] = email.utils.formataddr(('Recipient', self.to_email))
        msg['From'] = email.utils.formataddr(('no_reply.cm@bolagsverket.se', 'no_reply.cm@bolagsverket.se'))
        msg['Subject'] = mesg

        try:
            self.server.set_debuglevel(True)

            # identify ourselves, prompting server for supported features
            self.server.ehlo()

           # If we can encrypt this session, do it
            if self.server.has_extn('STARTTLS'):
                self.server.starttls()
                self.server.ehlo() # re-identify ourselves over TLS connection

#            self.server.login(self.username, self.password)
            print 'addressess:', self.to_email
            self.server.sendmail('no_reply.cm@bolagsverket.se', self.to_email, msg.as_string())
        finally:
            self.server.quit()

