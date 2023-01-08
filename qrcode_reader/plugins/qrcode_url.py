import re
import webbrowser
from tkinter import messagebox
import plugins 



class CodeQRUrl(plugins.Code):
	def __init__(self, _type, _subtype, _data):
		self.type = _type
		self.subtype = 'url'
		self.data = _data
		self.name = "Website"
		self.url = None
		super().__init__(self.type, self.subtype, self.data)


	def check(self):    
		try:
			if result := re.search(r'^(http|https):\/\/.*$', self.data):
				self.url = result.groups(0)
			elif result := re.search(r'^URLTO:(.*)$', self.data):
				self.url = result.groups(1)
			else: 
				return False
			return True
		except Exception as e:
			print(e)


	def actions(self):
		res = messagebox.askyesno(self.name, f"Open {self.url} ?")
		if res:
			webbrowser.open(self.tel)	
