import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
from plugins import QRCode



class QRCodeManager:
	def __init__(self):
		self.data = None


	def run(self):
		cap = cv2.VideoCapture(0)
		font = cv2.FONT_HERSHEY_PLAIN
		reading = True
		obj = None
		while reading:
			_, frame = cap.read()
			cv2.imshow('QRcode reader', frame)
			decodedObjects = pyzbar.decode(frame)
			for obj in decodedObjects:
				#print(obj)
				reading = False
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		self.data = obj.data.decode("utf-8")
		#print(self.data)	
		self.process_data()
		cap.release()
		cv2.destroyAllWindows()	


	def process_data(self):
		for p in QRCode._plugins:
			inst = p(self.data)
