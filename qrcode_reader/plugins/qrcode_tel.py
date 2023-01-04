import re
import webbrowser
from tkinter import messagebox
import plugins 



class QRCodeTel(plugins.QRCode):
	def __init__(self, _data):
		self.type = 'tel'
		self.data = _data
		self.tel = None
		self.name = "Telephone"
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


	def actions(self):
		res = messagebox.askyesno(self.name, f"Call {self.tel} ?")
		if res:
			webbrowser.open(self.tel)	