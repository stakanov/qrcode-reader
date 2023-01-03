import re
import webbrowser
from tkinter import messagebox
from qrcode_reader.plugins.QRCode import QRCode

class QRCodeMail(QRCode):
	def __init__(self, _data):
		self.type = 'email'
		self.data = _data
		self.address = None
		self.cc = None
		self.bcc = None
		self.subject = None
		self.body = None
		super().__init__(self.type, self.data)


	# def info(self):
	# 	print("="*80)
	# 	print(f"Type    : {self.type}")
	# 	print(f"Data    : {self.data}")
	# 	print(f"Address : {self.address}")
	# 	print(f"CC      : {self.cc}")
	# 	print(f"BCC     : {self.bcc}")
	# 	print(f"Subject : {self.subject}")
	# 	print(f"Body    : {self.body}")
	# 	print("="*80)

	def check(self):    
		try:
			if result := re.search(r'^mailto:(.*@.*\..*)\?(.*)$', self.data):
				self.address = result.groups()[0]
				self.args = result.groups()[1]
				for a in self.args.split('&'):
					k,v = a.split('=')
					if k == 'cc': self.cc = v
					if k == 'bcc': self.bbc = v
					if k == 'subject': self.subject = v
					if k == 'body': self.body = v
			else: 
				return False
			return True
		except Exception as e:
			print(e)

	def run(self):
		self.info()
		res = messagebox.askyesno('Send E-Mail', f"Send mail to {self.address} ?")
		if res:
			webbrowser.open(self.data)	    