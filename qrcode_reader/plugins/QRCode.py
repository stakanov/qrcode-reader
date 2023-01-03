import inspect

class QRCode:
	def __init__(self, _type, _data):
		self.type = _type
		self.data = _data
		if self.check():
			self.run()

	def info(self):
		for m in inspect.getmembers(self):
			if not m[0].startswith('_'):
				if not inspect.ismethod(m[1]):
					print(f"{m[0]}: {m[1]}")

