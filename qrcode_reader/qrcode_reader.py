#!/usr/bin/env python3

from qrcode_manager import QRCodeManager


def main():
	app = QRCodeManager()
	app.run()

if __name__=="__main__":
	print("Starting...")
	main()
	print("Done.")