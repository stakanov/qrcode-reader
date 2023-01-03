import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
#import re
#import sys

from qrcode_reader.plugins.QRCodeUrl import QRCodeUrl
from qrcode_reader.plugins.QRCodeWifi import QRCodeWifi
from qrcode_reader.plugins.QRCodeMail import QRCodeMail
from qrcode_reader.plugins.QRCodeTel import QRCodeTel
from qrcode_reader.plugins.QRCodeSMS import QRCodeSMS


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
		print(self.data)	
		self.process_data()
		cap.release()
		cv2.destroyAllWindows()	

	def process_data(self):
		QRCodeUrl(self.data)
		QRCodeWifi(self.data)
		QRCodeMail(self.data)
		QRCodeTel(self.data)
		QRCodeSMS(self.data)
		"""
		if result := re.search(r'^(http|https):\/\/.*$', self.data):
			QRCode = QRCodeUrl(result.groups(0))
		elif result := re.search(r'^URLTO:(.*)$', self.data):
			QRCode = QRCodeUrl(result.groups(1))
		else:
			print("QRCode not supported!")
			sys.exit(0)
		"""
		
