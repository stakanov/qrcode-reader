import re
import webbrowser
from tkinter import messagebox
import plugins 



class QRCodeUrl(plugins.QRCode):
	def __init__(self, _data):
		self.type = 'url'
		self.data = _data
		self.name = "Website"
		self.url = None
		super().__init__(self.type, self.data)


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
