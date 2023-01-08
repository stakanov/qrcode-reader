import re
import webbrowser
from tkinter import messagebox
import plugins 



class CodeQRContat(plugins.Code):
	def __init__(self, _type, _subtype, _data):
		self.type = _type
		self.subtype = 'contact'
		self.data = _data
		self.name = "Contact"
		super().__init__(self.type, self.subtype, self.data)


	def check(self):    
		try:
			if result := re.search(r'^BEGIN:VCARD.*', self.data):
				return True
				#lines = result.groups()[0].split('\n')
				#if lines[1] == 'VERSION:3.0':
				#	for l in lines[2:]:
			else: 
				return False
			return True
		except Exception as e:
			print(e)


	def actions(self):
		msg = f"Contact card: {self.data}"
		res = messagebox.showinfo(self.name, msg)
		print(f"{self.name}: {msg}")
		