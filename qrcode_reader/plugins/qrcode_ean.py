import re
import webbrowser
from tkinter import messagebox
import plugins 



class EAN(plugins.Code):
	def __init__(self, _type, _subtype, _data):
		self.type = _type
		self.subtype = None
		self.data = _data
		self.name = "EAN"
		super().__init__(self.type, self.subtype, self.data)


	def check(self):    
		try:
			if len(self.data) == 13:
				self.name = "EAN-13"
			elif len(self.data) == 8:
				self.name = "EAN-8"
			else: 
				return False
			return True
		except Exception as e:
			print(e)


	def actions(self):
		msg = f"Read: {self.data}"
		messagebox.showinfo(self.name, msg)
		print(f"{self.name}: {msg}")
