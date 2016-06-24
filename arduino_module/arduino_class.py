#from  arduino_module import app
import serial
import json
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
		new_dict = {}
		# remove ":" from port name
		for each_port in port_list:
			list_one = list(each_port)

			list_one = [ x for x in list_one if x !=":"]
			list_one = join(list_one)
			new_list.append(list_one)

		for each_value in new_list:
			print each_value
			new_dict[str(new_list.index(each_value))] = str(each_value)

		

		port_list = new_dict
		return json.dumps(port_list)
if __name__ == '__main__':
	test = ard_get_data()
	print test.port_scan()

'''
@app.route('/')
@app.route('/index')
def index():
	return "hello"
@app.route('/serial')
def get_serial_info():
	SERIAL_CONF_FILE = "serial.json"
	try:

		open_file = open(SERIAL_CONF_FILE,'r')
	except IOError:
		return "can not find file or directory"

	else:	
		json_date = json.load(open_file)
		json_date = str(json_date)
		return json_date


@app.route('/serial_data')
def show_serial_data():
	
	ser = serial.Serial(port='/dev/ttyACM0',baudrate=9600)

	try:
		a = ser.readline()
	except IOError as e:
		return "port error"
		exit()
	else:
		return a
		'''