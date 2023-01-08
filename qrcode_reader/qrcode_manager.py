import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
from plugins import Code



class CodeManager:
	def __init__(self):
		self.type = None
		self.subtype = None
		self.data = None


	def run(self):
		cap = cv2.VideoCapture(0)
		font = cv2.FONT_HERSHEY_PLAIN
		reading = True
		obj = None
		while reading:
			_, frame = cap.read()
			cv2.imshow('Code reader', frame)
			decodedObjects = pyzbar.decode(frame)
			for obj in decodedObjects:
				#print(obj)
				reading = False
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		print(obj)
		if obj != None:
			self.data = obj.data.decode("utf-8")
			self.type = obj.type
		self.process_data()
		cap.release()
		cv2.destroyAllWindows()	


	def process_data(self):
		for p in Code._plugins:
			inst = p(self.type, self.subtype, self.data)
