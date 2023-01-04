import re
import webbrowser
from tkinter import messagebox
import plugins 



class QRCodeMail(plugins.QRCode):
	def __init__(self, _data):
		self.type = 'email'
		self.data = _data
		self.name = "E-Mail"
		self.address = None
		self.cc = None
		self.bcc = None
		self.subject = None
		self.body = None
		super().__init__(self.type, self.data)


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


	def actions(self):
		res = messagebox.askyesno(self.name, f"Send mail to {self.address} ?")
		if res:
			webbrowser.open(self.data)	    