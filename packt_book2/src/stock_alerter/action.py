
class PrintAction:
	def execute(self, content):
		print(content)

"""
import smtp
from email.mime.text import MIMEText


class EmailAction:
	"Send a mail when rule is matched"
	from_email = "nfredrik@hotmail.com"
	def __init__(self, to):
		self.to_email = to

	def execute(self, content):
		message = MIMEText(content)
		message["Subject"] = "New Stock Alert"
		message["From"] = self.from_email
		message['To'] = self.to_email
		smtp = smtplib.SMTP("email.stocks.com")
		try:
			smtp.send_message(message)
		except:
			print ("EmailAction: Failed to send mail")
		finally:
			smtp.quit()

"""
