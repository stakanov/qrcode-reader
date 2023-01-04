import re
import webbrowser
from tkinter import messagebox
import plugins 



class QRCodeSMS(plugins.QRCode):
	def __init__(self, _data):
		self.type = 'sms'
		self.data = _data
		self.tel = None
		self.name = "SMS"
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
   

	def actions(self):
		res = messagebox.askyesno(self.name, f"Send SMS to {self.tel} with text: '{self.text}'?")
		if res:
			webbrowser.open(self.tel)	    