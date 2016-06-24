
import subprocess

class ard_get_data:
	def __init__(self):
		self.DEVICE_INFO = "serial.json"
		self.SERIAL_SCAN = "dmesg | grep 'tty' | awk '{ print $4 }' | grep '^tty'"

	def get_data(self):
		pass
	def port_scan(self):
		port_list = list(subprocess.check_output([self.SERIAL_SCAN], shell=True).split())
		port_list = set(port_list)
		new_list = []
		for each_port in port_list:
			list_one = list(each_port)
			try:
				if ":" in list_one:
					list_one.remove(":")
			except ValueError:
				pass
			else:
				list_one = ''.join(list_one)
			new_list.append(list_one)
		port_list = new_list
		return port_list



