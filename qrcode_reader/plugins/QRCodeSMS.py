import re
import webbrowser
from tkinter import messagebox
from qrcode_reader.plugins.QRCode import QRCode



class QRCodeSMS(QRCode):
	def __init__(self, _data):
		self.type = 'sms'
		self.data = _data
		self.tel = None
		super().__init__(self.type, self.data)


	def check(self):    
		try:
			if result := re.search(r'^(sms|smsto):([+\-\d]*):*(.*)$', self.data):
				self.tel = result.groups()[1]
				if len(result.groups()) > 2:
					self.text = result.groups()[2]
			else: 
				return False
			return True
		except Exception as e:
			print(e)


	def run(self):
		self.info()
		print(f"SMS to {self.tel}?")
		res = messagebox.askyesno('Send SMS', f"Send SMS to {self.tel} with text: '{self.text}'?")
		if res:
			webbrowser.open(self.tel)	    