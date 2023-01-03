import re
import webbrowser
from tkinter import messagebox
from qrcode_reader.plugins.QRCode import QRCode

class QRCodeUrl(QRCode):
	def __init__(self, _data):
		self.type = 'url'
		self.data = _data
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

	def run(self):
		self.info()
		print(f"Open {self.data}?")
		res = messagebox.askyesno('Open URL', f"Open {self.url} ?")
		if res:
			webbrowser.open(self.url)	    