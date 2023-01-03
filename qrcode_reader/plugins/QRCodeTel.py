import re
import webbrowser
from tkinter import messagebox
from qrcode_reader.plugins.QRCode import QRCode



class QRCodeTel(QRCode):
	def __init__(self, _data):
		self.type = 'tel'
		self.data = _data
		self.tel = None
		super().__init__(self.type, self.data)


	def check(self):    
		try:
			if result := re.search(r'^tel:(.*)$', self.data):
				self.tel = result.groups()[0]
			else: 
				return False
			return True
		except Exception as e:
			print(e)


	def run(self):
		self.info()
		print(f"Call {self.tel}?")
		res = messagebox.askyesno('Call telephone number', f"Call {self.tel} ?")
		if res:
			webbrowser.open(self.tel)	    