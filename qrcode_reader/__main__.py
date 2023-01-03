#!/usr/bin/env python3

from qrcode_reader import QRCodeManager

def main():
	app = QRCodeManager.QRCodeManager()
	app.run()

if __name__=="__main__":
	main()