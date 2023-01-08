import re
import webbrowser
from tkinter import messagebox
import gi
gi.require_version("NM", "1.0")
from gi.repository import GLib, NM
import sys, uuid
import plugins 



class CodeQRWifi(plugins.Code):
	def __init__(self, _type, _subtype, _data):
		self.type = _type
		self.subtype = 'wifi'
		self.data = _data
		self.name = "WiFi Connection"
		self.enc = None
		self.password = None
		self.ssid = None
		self.hidden = None
		self._main_loop = None
		super().__init__(self.type, self.subtype, self.data)		


	def check(self):
		try:
			if result := re.search(r'^WIFI:T:(WEP|WPA|);P:(.*);S:(.*);H:(true|false|);$', self.data):
				self.enc, self.password, self.ssid, self.hidden = result.groups()
			else:
				return False
			return True
		except Exception as e:
			print(e)
			

	def actions(self):
		res = messagebox.askyesno(self.name, f"Connect to {self.ssid}?")
		if res:		
			try:
				client = NM.Client.new(None)
				# Check if already exists
				if client.get_connection_by_id(self.ssid):
					msg = "Connessione già configurata. Niente da fare."
					res = messagebox.showwarning(self.name, msg)
				else:
					self._main_loop = GLib.MainLoop() 
					print("Creo la connessione...")
					connection = self.create_connection()
					client.add_connection_async(connection, True, None, self.added_cb, None)
					self._main_loop.run()
					msg = f"Connessione {self.ssid} creata!"
					messagebox.showinfo(self.name, msg)
			except Exception as e:
				msg = f"Errore creazione connessione: {e}"
				messagebox.showerror(self.name, msg)


	def create_connection(self):
		try:
			connection = NM.SimpleConnection.new()
			s_con = NM.SettingConnection.new()
			s_con.set_property(NM.SETTING_CONNECTION_ID, self.ssid)
			s_con.set_property(NM.SETTING_CONNECTION_UUID, str(uuid.uuid4()))
			s_con.set_property(NM.SETTING_CONNECTION_TYPE, "802-11-wireless")
			s_wifi = NM.SettingWireless.new()
			s_wifi.set_property(NM.SETTING_WIRELESS_SSID, GLib.Bytes.new(self.ssid.encode("utf-8")))
			s_wifi.set_property(NM.SETTING_WIRELESS_MODE, "infrastructure")
			s_wsec = NM.SettingWirelessSecurity.new()
			if self.enc == "WPA":
				s_wsec.set_property(NM.SETTING_WIRELESS_SECURITY_KEY_MGMT, "wpa-psk")
			elif self.enc == "WEP":
				s_wsec.set_property(NM.SETTING_WIRELESS_SECURITY_KEY_MGMT, "wep")
			else:
				s_wsec.set_property(NM.SETTING_WIRELESS_SECURITY_KEY_MGMT, "")
			s_wsec.set_property(NM.SETTING_WIRELESS_SECURITY_PSK, self.password)
			s_ip4 = NM.SettingIP4Config.new()
			s_ip4.set_property(NM.SETTING_IP_CONFIG_METHOD, "auto")
			s_ip6 = NM.SettingIP6Config.new()
			s_ip6.set_property(NM.SETTING_IP_CONFIG_METHOD, "auto")
			connection.add_setting(s_con)
			connection.add_setting(s_wifi)
			connection.add_setting(s_wsec)
			connection.add_setting(s_ip4)
			connection.add_setting(s_ip6)
			#print(f"Created connection profile: {self.ssid}")
			#connection.for_each_setting_value(self.print_values, None)
			return connection
		except Exception as e:
			raise(e)


	def print_values(self, setting, key, value, flags, data):
		print("  %s.%s: %s" % (setting.get_name(), key, value))


	def added_cb(self, client, result, data):
		try:
			client.add_connection_finish(result)
			print("The connection profile has been successfully added to NetworkManager.")
		except Exception as e:
			sys.stderr.write("Error: %s\n" % e)
		self.main_loop.quit()