#!/usr/bin/env python3

from qrcode_manager import CodeManager


def main():
	app = CodeManager()
	app.run()

if __name__=="__main__":
	print("Starting...")
	main()
	print("Done.")